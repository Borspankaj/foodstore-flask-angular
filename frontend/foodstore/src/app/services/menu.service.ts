import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class MenuService {

  private apiUrl = 'http://127.0.0.1:4000/api';
  constructor(
    private http: HttpClient ,
  ) { }

  addMenu(menuData: any , restaurantId : any): Observable<any> {
    
    const payload ={
      'dish_name' : menuData.dishName ,
      'price' : menuData.price ,
      'description' : menuData.description ,
      'restaurant_id' : restaurantId
    }
    const url = `${this.apiUrl}/menu`;
    return this.http.post(url, payload );
  }

  getMenu(menuId : any) : Observable<any> {
    const url = `${this.apiUrl}/menu/${menuId}`
    return this.http.get(url)

  }

  updateMenu(menu : any) : Observable<any>{

    const url = `${this.apiUrl}/menu/${menu.menu_id}`
    return this.http.put(url , menu)

  }

  deleteMenu(menuId : any) : Observable<any>{

    const url = `${this.apiUrl}/menu/${menuId}`
    return this.http.delete(url)

  }
}
