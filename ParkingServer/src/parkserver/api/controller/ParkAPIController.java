package parkserver.api.controller;

import java.io.IOException;
import java.io.PrintWriter;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.concurrent.TimeUnit;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.google.gson.Gson;

import parkserver.api.dao.ParkingDao;
import parkserver.api.model.ParkCar;
import parkserver.api.service.ParkingService;
import parkserver.api.service.ParkingServiceImpl;

public class ParkAPIController extends HttpServlet {
	
	public static ParkingService service = ParkingServiceImpl.getInstance();

	@Override
	protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		String url = req.getRequestURI();
		String contextPath = req.getContextPath();
		
		String command = url.split("/")[3];
		
		System.out.println( command );
		
		if( command.equals("search") ) {
			searchCar(req, resp);
		}else if( command.equals("list")) {
			parkingList(req, resp);
		}else if( command.equals("payment")) {
			paymentParking(req, resp);
		}
	}
	
	private void searchCar(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException{
		ParkingDao dao = ParkingDao.getInstence();
		ParkCar car = new ParkCar();
		
		String carNumber = req.getParameter("car_number");
		car.setCarNumber(carNumber);
		
		car = dao.selectCar(car);
		
		SimpleDateFormat format = new SimpleDateFormat("YYYY-MM-DD HH:mm:ss");
		Date enter = null;
		Date exit = null;
		
		System.out.println(car.getEnterTime());
		try {
			enter = format.parse(car.getEnterTime());
			exit = new Date();
		}catch (Exception e) {
			e.printStackTrace();
		}
		
		long diff = exit.getTime() - enter.getTime();
		long minute = TimeUnit.MILLISECONDS.toMinutes(diff);
		System.out.println(minute);
		
		car.setParkingPrice( (int)( minute * 100) );
		Gson gson = new Gson();
		resp.setContentType("application/json; charset=utf-8");
		PrintWriter wr = resp.getWriter();
		wr.append(gson.toJson(car));
		
	}
	
	private void parkingList( HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException{
		ParkingDao dao = ParkingDao.getInstence();
		List<ParkCar> returnList = dao.selectParkingInfo(new ParkCar());
		resp.setContentType("application/json; charset=utf-8");
		PrintWriter wt = resp.getWriter();
		Gson gson = new Gson();
		wt.append(gson.toJson(returnList));
	} 
	
	private void paymentParking(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		int id = Integer.parseInt(req.getParameter("id") ) ;
		ParkingDao dao = ParkingDao.getInstence();
		ParkCar car = new ParkCar();
		car.setId(id);
		dao.updatePay(car);
	}
	
}
