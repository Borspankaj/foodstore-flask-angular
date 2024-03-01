import { Component } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { Router } from '@angular/router';
@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent {
  email: string = '';
  password: string = '';
  errorMessage: string = '';

  constructor(private authService : AuthService , private router: Router) {}

  onSubmit() {
    console.log(this.email , this.password)
    this.authService.login(this.email, this.password).subscribe(
      (response) => {
        console.log('Authentication successful:', response);
        this.authService.extractTokenAndRole(response)
        const role = sessionStorage.getItem('role') 
        if (role == "Customer") 
          this.router.navigate(['/home']);
        else
          this.router.navigate(['/owner-home'])
      },
      (error) => {
        console.error('Authentication failed:', error);
        this.errorMessage = 'Invalid email or password'; 
      }
    );
  }

  navigateToRegister() {
    
    this.router.navigate(['/register-user']);
  }

}
