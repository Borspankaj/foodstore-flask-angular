import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { RestaurantService } from 'src/app/services/restaurant.service';
@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css']
})
export class HomePageComponent {
  restaurants: any;
  searchKeyword: any;

  constructor(
    private restaurantService: RestaurantService,
    private router : Router) {}

  ngOnInit() {
    this.loadRestaurants();
  }

  loadRestaurants() {
    this.restaurantService.getAllRestaurants().subscribe(
      (data) => {
        this.restaurants = data.data;
        console.log(this.restaurants)
      },
      (error) => {
        console.error('Error fetching restaurants:', error);
      }
    );
  }
  onSearch() {
    console.log('Search Keyword:', this.searchKeyword);

    this.restaurantService.searchRestaurants(this.searchKeyword).subscribe(
      (data) => {
        this.restaurants = data.data;
        console.log('Search results:', this.restaurants);
      },
      (error) => {
        console.error('Error searching restaurants:', error);
      }
    );
  }

  viewDetails(restaurant_id : any) {
    this.router.navigate(['/restaurant', restaurant_id]);
      
  }

}
