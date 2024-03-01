import { Component } from '@angular/core';
import { AccountService } from 'src/app/services/account.service';
import { AuthService } from 'src/app/services/auth.service';
import { Router } from '@angular/router';
@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent {

  constructor(
    private authService: AuthService ,
    private router : Router ,
    private accountService : AccountService) {
      
    }
    logout() {
      this.authService.logout().subscribe(
        (response) => {
          console.log('Logout successful:', response);
          sessionStorage.clear()
          localStorage.clear()
          this.router.navigate(['/'])
        },
        (error) => {
          console.error('Logout failed:', error);
          
        }
      );
    }

    viewCart() {
      this.router.navigate(['/mycart']);
    }
    viewOrders() {
      this.router.navigate(['/myorders'])
    }
  
    isLoggedIn() {
      return this.accountService.isLoggedIn()
    }
  
    getRole() {
      return this.accountService.getRole()
    }
  goToHome() {
    const role = this.accountService.getRole()
    if (role == "Owner") this.router.navigate(['/owner-home'])
    else this.router.navigate(['/home'])
  }


}
