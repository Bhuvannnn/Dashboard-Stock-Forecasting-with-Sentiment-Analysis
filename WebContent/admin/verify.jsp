<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1" import="java.sql.*"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<%

		String s3 = request.getParameter("un");
		String s4 = request.getParameter("pw");
		String un = null;
		String pw = null;
		Class.forName("com.mysql.jdbc.Driver");
		
		Connection c = DriverManager.getConnection("jdbc:mysql://localhost/prompt","root","root");
		Statement s = c.createStatement();
		ResultSet r = s.executeQuery("SELECT * FROM user where un='"+s3+"' and pw='"+s4+"' ");
		
		if(r.next()){
			response.sendRedirect("index.jsp");
			session.setAttribute("un",s3);
		}
		else{
			response.sendRedirect("login.jsp");
			session.setAttribute("error","user or password wrong or doesnt exist");
		}
	%>
</body>
</html>