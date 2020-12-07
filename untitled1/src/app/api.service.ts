import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor( private http: HttpClient ) { }
  getapi() {
    return this.http.get('https://31ps5t3oc2.execute-api.us-west-1.amazonaws.com/default/datafroms3');
  }
}
