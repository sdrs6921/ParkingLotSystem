package parkserver.api.service;

import java.util.List;

import parkserver.api.model.ParkCar;

public interface ParkingService {
	
	public List<ParkCar> parkingList(ParkCar car);
	
	public int paymentParkingCar(ParkCar car);
	
	public int enterCar(ParkCar car);
	
	public int exitCar(ParkCar car);
	
	public ParkCar searchCar(ParkCar car);
	
}
