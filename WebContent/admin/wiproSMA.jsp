<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>

<html lang="en" class="light-style layout-menu-fixed" dir="ltr"
	data-theme="theme-default" data-assets-path="adminResources/"
	data-template="vertical-menu-template-free">
<head>
<meta charset="utf-8" />
<meta name="viewport"
	content="width=device-width, initial-scale=1.0, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0" />

<title>Prompt Softech</title>

<meta name="description" content="" />

<!-- Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link
	href="https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap"
	rel="stylesheet" />

<!-- Icons. Uncomment required icon fonts -->
<link rel="stylesheet" href="adminResources/css/boxicons.css" />

<!-- Core CSS -->
<link rel="stylesheet" href="adminResources/css/core.css"
	class="template-customizer-core-css" />
<link rel="stylesheet" href="adminResources/css/theme-default.css"
	class="template-customizer-theme-css" />
<link rel="stylesheet" href="adminResources/css/demo.css" />

<!-- Vendors CSS -->
<link rel="stylesheet" href="adminResources/css/perfect-scrollbar.css" />

<link rel="stylesheet" href="adminResources/css/apex-charts.css" />

<!-- Page CSS -->

<!-- Helpers -->
<script src="adminResources/js/helpers.js"></script>

<!--! Template customizer & Theme config files MUST be included after core stylesheets and helpers.js in the <head> section -->
<!--? Config:  Mandatory theme config file contain global vars & default theme options, Set your preferred theme option in this file.  -->
<script src="adminResources/js/config.js"></script>
</head>

<body>
	<!-- Layout wrapper -->
	<div class="layout-wrapper layout-content-navbar">
		<div class="layout-container">
			<!-- Menu -->
			<jsp:include page="menu.jsp" />
			<!-- / Menu -->

			<!-- Layout container -->
			<div class="layout-page">

				<!-- Navbar -->
				<jsp:include page="header.jsp" />
				<!-- / Navbar -->

				<!-- Content wrapper -->
				<div class="content-wrapper">
					<!-- Content -->
					<div class="container-xxl flex-grow-1 container-p-y">
						<div class="row">
							<%@include file="sma of wipro.ns .html"%>
						</div>
						
					</div>
					<!-- Footer -->
					<jsp:include page="footer.jsp" />
					<!-- / Footer -->

					<div class="content-backdrop fade"></div>
				</div>
				<!-- Content wrapper -->
			</div>
		</div>
		<div class="layout-overlay layout-menu-toggle"></div>
	</div>
	<!-- / Layout page -->

	<!-- Overlay -->
	<div class="layout-overlay layout-menu-toggle"></div>
	<!-- / Layout wrapper -->



	<!-- Core JS -->
	<!-- build:js assets/vendor/js/core.js -->
	<script src="adminResources/js/jquery.js"></script>
	<script src="adminResources/js/popper.js"></script>
	<script src="adminResources/js/bootstrap.js"></script>


	<script
		src="adminResources/vendor/libs/perfect-scrollbar/perfect-scrollbar.js"></script>
	<script src="adminResources/js/menu.js"></script>
	<!-- endbuild -->

	<!-- Vendors JS -->
	<script src="adminResources/js/apexcharts.js"></script>

	<!--   Main JS -->
	<script src="adminResources/js/main.js"></script>

	<!-- Page JS -->
	<script src="adminResources/js/dashboards-analytics.js"></script>

	<!--  Place this tag in your head or just before your close body tag. -->
	<script async defer src="https://buttons.github.io/buttons.js"></script>
	-->
</body>
</html>
