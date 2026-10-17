import java.nio.file.*;
import java.net.*;
import java.security.*;
public class PortableGuardProbe {
 @SuppressWarnings("removal") public static void main(String[]args)throws Exception{
  boolean net=false,write=false,exec=false,disable=false;
  try(Socket s=new Socket()){s.connect(new InetSocketAddress("127.0.0.1",61234),100);}catch(AccessControlException e){net=e.getPermission() instanceof SocketPermission;}
  try{Files.writeString(Path.of(args[0]),"must not exist");}catch(AccessControlException e){write=e.getPermission() instanceof java.io.FilePermission;}
  try{new ProcessBuilder("sh","-c","true").start();}catch(AccessControlException e){exec=e.getPermission() instanceof java.io.FilePermission;}
  try{System.setSecurityManager(null);}catch(AccessControlException e){disable=e.getPermission() instanceof RuntimePermission;}
  System.out.println("{\"network_blocked\":"+net+",\"file_write_blocked\":"+write+",\"process_execution_blocked\":"+exec+",\"guard_disable_blocked\":"+disable+"}");if(!net||!write||!exec||!disable)System.exit(1);
 }
}
