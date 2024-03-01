import { Component } from '@angular/core';
import { RestaurantService } from 'src/app/services/restaurant.service';
@Component({
  selector: 'app-register-restaurant',
  templateUrl: './register-restaurant.component.html',
  styleUrls: ['./register-restaurant.component.css']
})
export class RegisterRestaurantComponent {
  restaurant = {
    name: '',
    location: '',
    cuisine: ''
  };
  errorMessage: string = ''; 

  constructor(private restaurantService: RestaurantService) {}

  submitForm() {
    this.restaurantService.registerRestaurant(this.restaurant).subscribe(
      (response) => {
        console.log('Restaurant registered successfully:', response);
      },
      (error) => {
        this.errorMessage = 'Error ' + error.message;
        console.error('Error registering restaurant:', error); 
      }
    );
  }
}
