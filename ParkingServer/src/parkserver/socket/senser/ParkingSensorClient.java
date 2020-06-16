package parkserver.socket.senser;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.Socket;
import java.util.concurrent.BlockingQueue;

import parkserver.api.dao.ParkingDao;
import parkserver.api.model.ParkCar;

public class ParkingSensorClient extends Thread{
	
	private BlockingQueue<String> dataQueue = null;
	
	private Socket raspiSocket = null;
	
	private ParkingDao dao = ParkingDao.getInstence();

	public void setDataQueue(BlockingQueue<String> dataQueue) {
		this.dataQueue = dataQueue;
	}

	public void setRaspiSocket(Socket raspiSocket) {
		this.raspiSocket = raspiSocket;
	}

	@Override
	public void run() {
		System.out.println("Test Socket is run!");
		if( raspiSocket != null ) {
			InputStream input = null;
			InputStreamReader isr = null;
			BufferedReader br = null;
			try {
				input = raspiSocket.getInputStream();
				isr = new InputStreamReader(input , "UTF-8");
				br = new BufferedReader(isr);
			} catch (IOException e) {
				e.printStackTrace();
			}
			
	
			
			while(true) {
				System.out.println("receive data!");
				try {
					String data = br.readLine();
					System.out.println("put data : " + data);
					String[] parseData = data.split(":");
					ParkCar car = new ParkCar();
					car.setParkingPosition(parseData[0]);
					car.setCarNumber(parseData[1]);
					
					ParkCar test = dao.selectCar(car);
					if( !car.getCarNumber().equals("NULL") ) {
						System.out.println( "No Seach");
						dao.insertParkingInfo(car);
					}else {
						dao.updateExitTime(car);
					}
					
					
					dataQueue.put(data);
				} catch (IOException e) {
					break;
				} catch (InterruptedException e ) {
					e.printStackTrace();
				}
			}
		}
		
	}
	
	
	
	
	

}
