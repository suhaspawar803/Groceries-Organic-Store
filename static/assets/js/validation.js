
//  REgister Code
    document.addEventListener('DOMContentLoaded', function() {
        // Toggle between Customer and Seller forms
        document.getElementById('customer-form-link').addEventListener('click', function() {
            document.getElementById('customer-form').style.display = 'block';
            document.getElementById('seller-form').style.display = 'none';
        });
    
        document.getElementById('seller-form-link').addEventListener('click', function() {
            document.getElementById('customer-form').style.display = 'none';
            document.getElementById('seller-form').style.display = 'block';
        });
    
        // Handle Email Verification for Customer
        document.getElementById('verify-customer-email').addEventListener('click', function() {
            var email = document.getElementById('customer_email').value;
            if (email) {
                fetch("/send_otp/", {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify({ email: email })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        document.getElementById('customer-otp-field').style.display = 'block';
                        document.getElementById('register-submit').disabled = true;
                        alert('OTP sent to your email.');
                    } else {
                        alert('Failed to send OTP.');
                    }
                })
                .catch(error => console.error('Error:', error));
            } else {
                alert('Please enter an email address.');
            }
        });
    
        // Handle OTP Verification for Customer
        document.getElementById('customer_otp').addEventListener('blur', function() {
            var otp = document.getElementById('customer_otp').value;
            var email = document.getElementById('customer_email').value;
    
            if (otp) {
                fetch("/verify_otp/", {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify({ otp: otp, email: email })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        document.getElementById('register-submit').disabled = false;
                    } else {
                        alert('Invalid OTP.');
                    }
                })
                .catch(error => console.error('Error:', error));
            }
        });
    
        
       // Handle Email Verification for Seller
    document.getElementById('verify-seller-email').addEventListener('click', function() {
        var email = document.getElementById('seller_email').value;
        if (email) {
            fetch("/send_otp/", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ email: email })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    document.getElementById('seller-otp-field').style.display = 'block';
                    document.getElementById('register-submit-seller').disabled = true;
                    alert('OTP sent to your email.');
                } else {
                    alert('Failed to send OTP.');
                }
            })
            .catch(error => console.error('Error:', error));
        } else {
            alert('Please enter an email address.');
        }
    });

    // Handle OTP Verification for Seller
    document.getElementById('seller_otp').addEventListener('blur', function() {
        var otp = document.getElementById('seller_otp').value;
        var email = document.getElementById('seller_email').value;

        if (otp) {
            fetch("/verify_otp/", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ otp: otp, email: email })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    document.getElementById('register-submit-seller').disabled = false;
                } else {
                    alert('Invalid OTP.');
                }
            })
            .catch(error => console.error('Error:', error));
        }
    });

        // Function to get CSRF token from cookies
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
    
        // Validate Customer Form
        document.getElementById('customer-form').addEventListener('submit', function(e) {
            var name = document.getElementById('customer_name').value;
            var mobileNumber = document.getElementById('customer_mobile_number').value;
            var password = document.getElementById('customer_password').value;
            var cpassword = document.getElementById('confirm_customer_password').value;
            var otpField = document.getElementById('customer-otp-field').style.display;
            var isOtpVerified = !document.getElementById('register-submit').disabled;
    
            // Check if OTP is verified and OTP field is visible
            if (otpField !== 'block' || !isOtpVerified) {
                alert('Please verify your email and OTP.');
                e.preventDefault();
                return;
            }
    
            // Validate Customer Name
            if (!/^[A-Z]/.test(name)) {
                alert('Customer name must start with a capital letter.');
                e.preventDefault();
                return;
            }
    
            // Validate Mobile Number
            if (!/^\d{10}$/.test(mobileNumber)) {
                alert('Mobile number must be exactly 10 digits.');
                e.preventDefault();
                return;
            }
    
            // Validate Password
            if (!/(?=.*\d)(?=.*[!@#$%^&*]).{4,}/.test(password)) {
                alert('Password must contain at least 4 characters, including at least one digit and one special symbol.');
                e.preventDefault();
                return;
            }
    
            // Confirm Password
            if (password !== cpassword) {
                alert('Passwords do not match.');
                e.preventDefault();
                return;
            }
        });
    
        // Validate Seller Form
        document.getElementById('seller-form').addEventListener('submit', function(e) {
            var name = document.getElementById('seller_name').value;
            var mobileNumber = document.getElementById('seller_mobile_number').value;
            var password = document.getElementById('seller_password').value;
            var cpassword = document.getElementById('confirm_seller_password').value;
            var otpField = document.getElementById('seller-otp-field').style.display;
            var isOtpVerified = !document.getElementById('register-submit-seller').disabled;
    
            // Check if OTP is verified and OTP field is visible
            if (otpField !== 'block' || !isOtpVerified) {
                alert('Please verify your email and OTP.');
                e.preventDefault();
                return;
            }
    
            // Validate Seller Name
            if (!/^[A-Z]/.test(name)) {
                alert('Seller name must start with a capital letter.');
                e.preventDefault();
                return;
            }
    
            // Validate Mobile Number
            if (!/^\d{10}$/.test(mobileNumber)) {
                alert('Mobile number must be exactly 10 digits.');
                e.preventDefault();
                return;
            }
    
            // Validate Password
            if (!/(?=.*\d)(?=.*[!@#$%^&*]).{4,}/.test(password)) {
                alert('Password must contain at least 4 characters, including at least one digit and one special symbol.');
                e.preventDefault();
                return;
            }
    
            // Confirm Password
            if (password !== cpassword) {
                alert('Passwords do not match.');
                e.preventDefault();
                return;
            }
        });
    });
   

/////////////////////////////////////////////////////////////////////////////////////

// login validation

    document.addEventListener('DOMContentLoaded', function() {
        var form = document.getElementById('login-form');

        form.addEventListener('submit', function(event) {
            var isValid = true;

            // Validate Role Selection
            var role = document.getElementById('role');
            if (!role.value) {
                role.classList.add('is-invalid');
                isValid = false;
            } else {
                role.classList.remove('is-invalid');
            }

            // Validate Email
            var email = document.getElementById('email');
            var emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            if (!emailPattern.test(email.value)) {
                email.classList.add('is-invalid');
                isValid = false;
            } else {
                email.classList.remove('is-invalid');
            }

            // Validate Password
            var password = document.getElementById('password');
            var passwordPattern = /^(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{4,}$/;
            if (!passwordPattern.test(password.value)) {
                password.classList.add('is-invalid');
                isValid = false;
            } else {
                password.classList.remove('is-invalid');
            }

            if (!isValid) {
                event.preventDefault(); // Prevent form submission if validation fails
                form.classList.add('was-validated');
            }
        });
    });
             

    


    //////////Register page//////////


    $(function() {

        $('#login-form-link').click(function(e) {
            $("#login-form").delay(100).fadeIn(100);
             $("#register-form").fadeOut(100);
            $('#register-form-link').removeClass('active');
            $(this).addClass('active');
            e.preventDefault();
        });
        $('#register-form-link').click(function(e) {
            $("#register-form").delay(100).fadeIn(100);
             $("#login-form").fadeOut(100);
            $('#login-form-link').removeClass('active');
            $(this).addClass('active');
            e.preventDefault();
        });
    
    });





    /*   Seller Details   */

    