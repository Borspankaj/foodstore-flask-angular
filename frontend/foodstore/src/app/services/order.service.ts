import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class OrderService {
  private apiUrl = 'http://127.0.0.1:4000/api';

  constructor(private http: HttpClient) {}

  getOrders(): Observable<any> {
    const user_email = sessionStorage.getItem('user');
    return this.http.get<any>(`${this.apiUrl}/order/${user_email}`);
  }
  getOrdersByOwner(): Observable<any> {
    const user_email = sessionStorage.getItem('user');
    const url = `${this.apiUrl}/manage-orders/${user_email}`;
    return this.http.get(url);
  }
  updateStatus(orderItemId : any , updatedStatus : any) :Observable<any>
  {

    const url = `${this.apiUrl}/order`;
    const payload = {
      'order_id' : orderItemId ,
      'order_status' : updatedStatus
    }
    return this.http.put(url , payload);

  }
  getOrdersByRestaurant(restaurantId : any): Observable<any> {
    const user_email = sessionStorage.getItem('user');
    const url = `${this.apiUrl}/manage-orders/${restaurantId}`;
    return this.http.get(url);
  }

}
