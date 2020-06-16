package parkserver.socket;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import parkserver.socket.senser.ParkingSensorClient;
import parkserver.socket.user.ParkingDisplayClient;

/**
 * Servlet implementation class SocketServer
 */
@WebServlet("/SocketServer")
public class SocketServer extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public SocketServer() {
        super();
        initSocketServer();
    }
    
    public static void initSocketServer() {
    	ServerSocket serverSocket = null;
    	Socket socket = null;
    	
    	BlockingQueue<String> testQueue = new ArrayBlockingQueue<String>(1000);
    	
    	try {
    		serverSocket = new ServerSocket(9999);
    		System.out.println("ServerSocket Start!");
    		ParkingDisplayClient displayClient = new ParkingDisplayClient();
    		displayClient.setDataQueue(testQueue);
    		System.out.println("Display Thread Start!");
    		displayClient.start();
    		
    		while(true) {
    			try {
    				Socket client = serverSocket.accept();
    				InputStreamReader isr = new InputStreamReader(client.getInputStream());
    				int classInt = isr.read();
    				System.out.println(classInt);
    				if( classInt == 49) {
    					System.out.println("Raspi Connect");
    					ParkingSensorClient test = new ParkingSensorClient();
            			test.setDataQueue(testQueue);
            			test.setRaspiSocket(client);
            			test.start();
    				}else if( classInt == 50 ) {
    					System.out.println("User Connect");
    					displayClient.addUser(client);
    				}
        			
        			
    			}catch (Exception e) {
					System.out.println(e.getMessage());
				}
    			
    		}
    		
    	}catch (Exception e) {
    		e.printStackTrace();
		}
    }

}
