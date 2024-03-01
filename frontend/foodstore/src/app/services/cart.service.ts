import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AccountService } from './account.service';
@Injectable({
  providedIn: 'root'
})
export class CartService {

  private apiUrl = 'http://127.0.0.1:4000/api'; 

  constructor(
    private http: HttpClient ,
    private accountService : AccountService) {}

    getCartItems(): Observable<any[]> {
      const user_email = sessionStorage.getItem('user')
      console.log(user_email)
      return this.http.get<any[]>(`${this.apiUrl}/cart/${user_email}`);
    }

  addToCart(menuId: number, quantity: number , restaurantId : any): Observable<any> {
    const email = this.accountService.getEmail()
    const payload = { menu_id: menuId, quantity: quantity , restaurant_id : restaurantId };
    console.log(payload)
    return this.http.post<any>(`${this.apiUrl}/cart-item/${email}`, payload);
  }

  deleteCartItem(bookId: any): Observable<any> {
    const user_email = sessionStorage.getItem('user');
    return this.http.delete(`${this.apiUrl}/cart/${user_email}/${bookId}`);
  }

  placeOrder(): Observable<any> {
    const user_email = sessionStorage.getItem('user');
    return this.http.post(`${this.apiUrl}/order`, { email: user_email });
  }
}
