<h1> 주차관리 서버 </h1>

소켓 및 RestfulAPI를 담당하는 서버입니다.<br>

RestfulAPI
Http 요청에 의하 동작? 하는 부분으로 기초적인 Java Servlet으로 구현 하였으며
보여지는 Web페이지는 가지고 있지 않고 request method는 GET
응답은 JSON형식으로 하여 DB관련 API를 구성하고 있습니다.

소켓 서버 
Request에 요청에 의해 실행 되어지게 만들어져있습니다.
사실상 Dao의 공유를 위해 같은 서버에서 실행되고
있기에 개별적으로 실행되어도 문제는 없습니다.


build 폴더는 업로드 하면 안됐는데... 되버렸습니다.
