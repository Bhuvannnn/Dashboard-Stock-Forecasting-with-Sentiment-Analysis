<!DOCTYPE html>

<html lang="en" class="light-style customizer-hide" dir="ltr"
	data-theme="theme-default" data-assets-path="../assets/"
	data-template="vertical-menu-template-free">
<head>
<meta charset="utf-8" />
<meta name="viewport"
	content="width=device-width, initial-scale=1.0, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0" />

<title>Prompt Softech</title>

<meta name="description" content="" />

<!-- Favicon -->
<!-- <link rel="icon" type="image/x-icon"
	href="adminResources/images/SAC.jpg" /> -->

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

<!-- Page CSS -->
<!-- Page -->
<link rel="stylesheet" href="adminResources/css/page-auth.css" />
<!-- Helpers -->
<script src="adminResources/js/helpers.js"></script>

<!--! Template customizer & Theme config files MUST be included after core stylesheets and helpers.js in the <head> section -->
<!--? Config:  Mandatory theme config file contain global vars & default theme options, Set your preferred theme option in this file.  -->
<script src="adminResources/js/config.js"></script>
</head>

<body>
	<!-- Content -->

	<div class="container-xxl">
		<div class="authentication-wrapper authentication-basic container-p-y">
			<div class="authentication-inner">
				<!-- Register Card -->
				<div class="card">
					<div class="card-body">
						<!-- Logo -->
						<div class="app-brand justify-content-center">
							<a href="index.jsp" class="app-brand-link gap-2">
								<span class="app-brand-text demo text-body fw-bolder">Prompt Softech</span>
							</a>
						</div>
						<!-- /Logo -->
						<h5 class="mb-2">Make Stock management easy and fun!</h5>
						<form id="formAuthentication" class="mb-3" action="save.jsp"
							method="POST">
							<div class="mb-3">
								<label for="username" class="form-label">First Name</label> <input
									type="text" class="form-control" id="fn" name="fn"
									placeholder="Enter your username" autofocus required />
							</div>
							<div class="mb-3">
								<label for="username" class="form-label">Last Name</label> <input
									type="text" class="form-control" id="ln" name="ln"
									placeholder="Enter your username" autofocus required />
							</div>
							<div class="mb-3">
								<label for="username" class="form-label">Username</label> <input
									type="text" class="form-control" id="un" name="un"
									placeholder="Enter your username" autofocus required />
							</div>

							<div class="mb-3 form-password-toggle">
								<label class="form-label" for="password">Password</label>
								<div class="input-group input-group-merge">
									<input type="password" id="pw" class="form-control" name="pw"
										placeholder="&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;&#xb7;"
										aria-describedby="password" /> <span
										class="input-group-text cursor-pointer"><i
										class="bx bx-hide" required></i></span>
								</div>
							</div>
							<!-- 	<input type="button" class="btn btn-primary d-grid w-100">Sign up</input> -->
							<input type="submit" class="btn btn-primary d-grid w-100"
								value="sign up">
						</form>

						<p class="text-center">
							<span>Already have an account?</span> <a href="login.jsp"> <span>Sign
									in instead</span>
							</a>
						</p>
					</div>
				</div>
				<!-- Register Card -->
			</div>
		</div>
	</div>

	<!-- / Content -->

	<!-- Core JS -->
	<!-- build:js assets/vendor/js/core.js -->
	<script src="adminResources/js/jquery.js"></script>
	<script src="adminResources/js/popper.js"></script>
	<script src="adminResources/js/bootstrap.js"></script>
	<script src="adminResources/js/perfect-scrollbar.js"></script>

	<script src="adminResources/js/menu.js"></script>
	<!-- endbuild -->
	`
	<!-- Vendors JS -->

	<!-- Main JS -->
	<script src="adminResources/js/main.js"></script>

	<!-- Page JS -->

	<!-- Place this tag in your head or just before your close body tag. -->
	<script async defer src="https://buttons.github.io/buttons.js"></script>
</body>
</body>
</html>
