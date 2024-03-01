import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { RestaurantService } from 'src/app/services/restaurant.service';
@Component({
  selector: 'app-owner-home',
  templateUrl: './owner-home.component.html',
  styleUrls: ['./owner-home.component.css']
})
export class OwnerHomeComponent {
  ownerRestaurants: any ;

  constructor(
    private router: Router ,
    private restaurantService : RestaurantService) {}

    ngOnInit() {
      this.fetchOwnerRestaurants();
    }
  registerRestaurant() {
    this.router.navigate(['/register-restaurant']);
  }

  fetchOwnerRestaurants() {
    this.restaurantService.getOwnerRestaurants().subscribe(
      (restaurants) => {
        this.ownerRestaurants = restaurants.data;
        console.log('Owner Restaurants:', this.ownerRestaurants);
      },
      (error) => {
        console.error('Error fetching owner restaurants:', error);
        
      }
    );
  }
  goToRestaurant(restaurantId : any) {
    this.router.navigate(['/restaurant', restaurantId]); 
  }

}
