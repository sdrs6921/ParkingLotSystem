package parkserver.api.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import parkserver.api.model.ParkCar;
import parkserver.dbconnection.MySqlConnector;

public class ParkingDao {
	private static ParkingDao parkingDao;
	private MySqlConnector mysqlDB = MySqlConnector.getInstance();
	
	private ParkingDao() {}
	
	public static ParkingDao getInstence() {
		if( parkingDao == null ) parkingDao = new ParkingDao();
		return parkingDao;
	}
	
	Connection conn;
	PreparedStatement pstmt;
	ResultSet rs;
	
	public synchronized int insertParkingInfo(ParkCar car) {
		int result = 0;
		try {
			conn = mysqlDB.getConnection();
			String query = "INSERT INTO parkingdb.parking_payment ( position, car_number, enter_time) "
					+ "VALUES (? , ? , now())";
			pstmt = conn.prepareStatement(query);
			
			pstmt.setString(1, car.getParkingPosition());
			pstmt.setString(2, car.getCarNumber() );
			
			result = pstmt.executeUpdate();
		}catch (Exception e) {
			System.out.println(e.getMessage());
		}finally {
		}
		return result;
	}
	
	public int deleteParkingInfo() {
		return 0;
	}
	
	public synchronized int updatePay(ParkCar car) {
		int result = 0;
		try {
			conn = mysqlDB.getConnection();
			String query = "UPDATE parkingdb.parking_payment SET payment='T' "
					+ "WHERE id=?";
			pstmt = conn.prepareStatement(query);
			
			pstmt.setInt(1, car.getId());
			
			result = pstmt.executeUpdate();
		}catch (Exception e) {
			System.out.println(e.getMessage());
		}
		
		return result;
	}
	
	public synchronized int updateExitTime(ParkCar car) {
		int result = 0;
		try {
			conn = mysqlDB.getConnection();
			String query = "UPDATE parkingdb.parking_payment SET exit_time=now() , price=2000 "
					+ "WHERE position=? AND exit_time IS NULL";
			pstmt = conn.prepareStatement(query);
			
			pstmt.setString(1, car.getParkingPosition());
			
			result = pstmt.executeUpdate();
		}catch (Exception e) {
			System.out.println(e.getMessage());
		}
		return result;
	}
	
	public List<ParkCar> selectParkingInfo(ParkCar car) {
		List<ParkCar> returnList = new ArrayList<ParkCar>();
		
		try {
			conn = mysqlDB.getConnection();
			String query = "SELECT * FROM parking_payment";
			pstmt = conn.prepareStatement(query);
			
			rs = pstmt.executeQuery();
			
			while( rs.next() ) {
				ParkCar selectCar = new ParkCar();
				selectCar.setId(rs.getInt("id"));
				selectCar.setCarNumber(rs.getString("car_number"));
				selectCar.setEnterTime(rs.getString("enter_time"));
				selectCar.setExitTime(rs.getString("exit_time"));
				selectCar.setParkingPosition(rs.getString("position"));;
				selectCar.setParkingPrice(rs.getInt("price"));
				selectCar.setPayment(rs.getString("payment"));
				returnList.add(selectCar);
			}
		}catch (Exception e) {
			e.printStackTrace();
		}
		return returnList;
	}
	
	public ParkCar selectCar(ParkCar car) {
		ParkCar selectCar = new ParkCar();
		try {
			conn = mysqlDB.getConnection();
			String query = "SELECT * FROM parking_payment WHERE car_number=? AND exit_time is Null";
			pstmt = conn.prepareStatement(query);
			pstmt.setString(1, car.getCarNumber());
			rs = pstmt.executeQuery();
			
			while( rs.next() ) {
				selectCar.setId(rs.getInt("id"));
				selectCar.setCarNumber(rs.getString("car_number"));
				selectCar.setEnterTime(rs.getString("enter_time"));
				selectCar.setExitTime(rs.getString("exit_time"));
				selectCar.setParkingPosition(rs.getString("position"));;
				selectCar.setParkingPrice(rs.getInt("price"));
				selectCar.setPayment(rs.getString("payment"));
			}
		}catch (Exception e) {
			e.printStackTrace();
		}
		
		return selectCar;
	}
}
