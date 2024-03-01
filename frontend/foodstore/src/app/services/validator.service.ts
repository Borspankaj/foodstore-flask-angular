import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ValidatorService {

  constructor() { }

  validateUserData(userData : any): any {
    if (
      !userData.email ||
      !userData.name ||
      !userData.password ||
      !userData.phoneNumber
    ) {
      
      return { 
        valid : false ,
        message :"Field is required" }
    }
    return {
      valid :true ,
      message :"Valid" }
  }
    
}
