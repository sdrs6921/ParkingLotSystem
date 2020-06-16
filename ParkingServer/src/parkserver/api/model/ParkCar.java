package parkserver.api.model;

import java.io.Serializable;

public class ParkCar implements Serializable{
	//아이디값
	private int id;
	//주차 위치 표시 값
	private String parkingPosition;
	//차번호
	private String carNumber;
	//출입시간
	private String enterTime;
	//출자시간
	private String exitTime;
	//주차비용
	private int parkingPrice;
	//결제 여부
	private String payment;
	
	
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getPayment() {
		return payment;
	}
	public void setPayment(String payment) {
		this.payment = payment;
	}
	public String getParkingPosition() {
		return parkingPosition;
	}
	public void setParkingPosition(String parkingPosition) {
		this.parkingPosition = parkingPosition;
	}
	public String getCarNumber() {
		return carNumber;
	}
	public void setCarNumber(String carNumber) {
		this.carNumber = carNumber;
	}
	public String getEnterTime() {
		return enterTime;
	}
	public void setEnterTime(String enterTime) {
		this.enterTime = enterTime;
	}
	public String getExitTime() {
		return exitTime;
	}
	public void setExitTime(String exitTime) {
		this.exitTime = exitTime;
	}
	public int getParkingPrice() {
		return parkingPrice;
	}
	public void setParkingPrice(int parkingPrice) {
		this.parkingPrice = parkingPrice;
	}
	
	@Override
	public String toString() {
		return "ParkCar [parkingPosition=" + parkingPosition + ", carNumber=" + carNumber + ", enterTime=" + enterTime
				+ ", exitTime=" + exitTime + ", parkingPrice=" + parkingPrice + "]";
	}
	
	
	
	
}
