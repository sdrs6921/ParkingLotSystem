package parkserver.socket.user;

import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.BlockingQueue;

public class ParkingDisplayClient extends Thread{
	private BlockingQueue<String> dataQueue = null;
	private List<Socket> userDisplaySocket = new ArrayList<Socket>();
	
	public void setDataQueue(BlockingQueue<String> dataQueue) {
		this.dataQueue = dataQueue;
	}
	
	public void addUser(Socket userSocket) {
		userDisplaySocket.add(userSocket);
	}
	
	@Override
	public void run() {
		
		while(true) {
			String data = null;
			try {
				data = dataQueue.take();
			} catch (InterruptedException e2) {
				e2.printStackTrace();
			}
			System.out.println("take data: " + data);
			
			for(Socket userSocket : userDisplaySocket) {
				if( userSocket.isConnected() ) {
					OutputStream output = null;
					try {
						output = userSocket.getOutputStream();
						PrintWriter writer = new PrintWriter(new OutputStreamWriter(output, "UTF-8"));
						writer.print(data);
						writer.flush();
					} catch (IOException e) {
						System.out.println( e.getMessage());
						try {
							output.close();
							userSocket.close();
							userDisplaySocket.remove(userSocket);
						} catch (IOException e1) {
							e1.printStackTrace();
						}
						
					}
				}else {
					try {
						userSocket.close();
						userDisplaySocket.remove(userSocket);
					} catch (IOException e1) {
						e1.printStackTrace();
					}
				}
			}
		}
	}
	
}
