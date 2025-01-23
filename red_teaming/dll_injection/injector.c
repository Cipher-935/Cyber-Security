
#include <Windows.h>

#include <stdio.h>

#include <stdlib.h>

int main(int argc, char* argv[]){
   if(argc != 3){          // This will get the count of the number of arguments passed + 1, default will be argv[0] which will be the program name
       printf("Please provide the process id and the dll path");
       return 1;
  }
  
  DWORD p_id = atoi(argv[1]); // Using ascci to int conversion to get the numeric pid of the target
  const char* dll_path = argv[2]; // Using a char pointer to store the dll path
  printf("PID: %d\n", p_id);
  printf("Dll Path: %s\n", dll_path);

  HANDLE hproc = OpenProcess(PROCESS_ALL_ACCESS, FALSE, p_id); // Opening the target process with Process all access, FALSE is that child cannot inherit the handle
  if(hproc == NULL){
          
       printf("Could not open Process");
       return 1;      
  }

  LPVOID remote_mem = VirtualAllocEx(hproc, NULL, strlen(dll_path) + 1, MEM_COMMIT|MEM_RESERVE, PAGE_READWRITE); // Allocating the memory in target process which is size of dll path+null
  if(remote_mem == NULL){

        printf("Could not commit the memory");
        CloseHandle(hproc);
        return 1;
  }

  if(!WriteProcessMemory(hproc, remote_mem, dll_path, strlen(dll_path) + 1, NULL)){
        
     printf("Could not write to the target process");
     VirtualFreeEx(hproc, remote_mem, 0, MEM_RELEASE);
     CloseHandle(hproc);
     return 1;
  }

  HMODULE hkernel32 = GetModuleHandleW(L"Kernel32");
  if(hkernel32 == NULL){
   
     printf("Could not load the Kernel 32 module");

     VirtualFreeEx(hproc, remote_mem, 0, MEM_RELEASE);

     CloseHandle(hproc);

     return 1;
  }
  FARPROC loadlib = GetProcAddress(hkernel32, "LoadLibraryA");
  if(loadlib == NULL){
    
    
     printf("Could not load the library");

     VirtualFreeEx(hproc, remote_mem, 0, MEM_RELEASE);

     CloseHandle(hproc);

     return 1;


  }
  HANDLE rthread = CreateRemoteThread(hproc, NULL, 0, (LPTHREAD_START_ROUTINE)loadlib, remote_mem, 0, NULL);
  if(rthread == NULL){
     
      printf("Could not create the remote thread");
      VirtualFreeEx(hproc, remote_mem, 0, MEM_RELEASE);
      CloseHandle(hproc);
      return 1;
   
  }
  WaitForSingleObject(rthread, INFINITE);
  CloseHandle(rthread);
  VirtualFreeEx(hproc, remote_mem, 0, MEM_RELEASE);
  CloseHandle(hproc);
  return 0;

}