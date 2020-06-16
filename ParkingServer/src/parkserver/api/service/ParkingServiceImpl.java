package parkserver.api.service;

import java.util.List;

import parkserver.api.dao.ParkingDao;
import parkserver.api.model.ParkCar;

public class ParkingServiceImpl implements ParkingService {
	private static ParkingDao dao = ParkingDao.getInstence();
	
	private static ParkingServiceImpl service = null;
	
	private ParkingServiceImpl() {
	}
	
	public static ParkingServiceImpl getInstance() {
		if( service == null  ) service = new ParkingServiceImpl();
		return service;
	}

	@Override
	public List<ParkCar> parkingList(ParkCar car) {
		List<ParkCar> returnList = dao.selectParkingInfo(car);
		return returnList;
	}
	
	

	@Override
	public ParkCar searchCar(ParkCar car) {
		ParkCar returnCar = dao.selectCar(car);
		returnCar.setParkingPrice(1000);
		return returnCar;
	}



	@Override
	public int paymentParkingCar(ParkCar car) {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public int enterCar(ParkCar car) {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public int exitCar(ParkCar car) {
		// TODO Auto-generated method stub
		return 0;
	}

}
