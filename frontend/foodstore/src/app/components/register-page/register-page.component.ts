import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from 'src/app/services/user.service';
import { ValidatorService } from 'src/app/services/validator.service';
@Component({
  selector: 'app-register-page',
  templateUrl: './register-page.component.html',
  styleUrls: ['./register-page.component.css']
})
export class RegisterPageComponent {
  errorMessage: string = '';
  user: any = {
    email: '',
    name: '',
    password: '',
    role: 'Customer', 
    phoneNumber: ''
  };

  constructor(
    private userService: UserService ,
    private router : Router ,
    private validatorService : ValidatorService) {}

  roles = ['Customer', 'Owner']; 
  register() {
    const isValid = this.validatorService.validateUserData(this.user)
    if (isValid.valid) {
      this.userService.registerUser(this.user).subscribe(
        (response) => {
          console.log('User Registration Successful:', response);
          this.router.navigate(["/"])
          
        },
        (error) => {
          console.error('User Registration Failed:', error);
          this.errorMessage = "Error Occured"          
        }
      );
    }
    else {
      this.errorMessage = isValid.message
    }

  }

}
