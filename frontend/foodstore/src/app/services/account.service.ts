import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AccountService {

  constructor() { }
  getRole(){
    return sessionStorage.getItem('role')
  }
  
  isLoggedIn() {
    const user = sessionStorage.getItem('user')
    if(user) {
      return true
    }
    return false 
  }
  getEmail() {
    return sessionStorage.getItem('user')
  }
}
