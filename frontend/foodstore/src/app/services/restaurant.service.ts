import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AccountService } from './account.service';
@Injectable({
  providedIn: 'root'
})
export class RestaurantService {

  private apiUrl = 'http://127.0.0.1:4000/api'; 

  constructor(
    private http: HttpClient ,
    private accountService : AccountService  ) {}

  
  getAllRestaurants(): Observable<any> {
    return this.http.get(`${this.apiUrl}/restaurants`);
  }

  
  getRestaurantById(restaurantId: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/restaurant/${restaurantId}`);
  }

  searchRestaurants(keyword: string): Observable<any> {
    const payload = {
      keyword
    }
    return this.http.post(`${this.apiUrl}/restaurants`, payload);
  }

  registerRestaurant(restaurantData: any): Observable<any> {
    
    const payload ={
      'name' : restaurantData.name ,
      'location' : restaurantData.location ,
      'cuisine' : restaurantData.cuisine ,
      'email' : this.accountService.getEmail()
    }
    const url = `${this.apiUrl}/restaurant`;
    return this.http.post(url, payload );
  }
  getRestaurantMenu(restaurantId : any): Observable<any> {
   
    const url = `${this.apiUrl}/get-restaurant-menu/${restaurantId}`;
    return this.http.get(url);
  }

  getOwnerRestaurants() : Observable<any>{
    const email = this.accountService.getEmail()
    const url = `${this.apiUrl}/owner-restaurants/${email}` ;
    
    return this.http.get(url) ;
  }
}
