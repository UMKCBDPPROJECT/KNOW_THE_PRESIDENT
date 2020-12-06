import { Component, OnInit } from '@angular/core';
// tslint:disable-next-line:import-spacing
import {ApiService} from '../api.service';

@Component({
  selector: 'app-tab-page',
  templateUrl: './tab-page.component.html',
  styleUrls: ['./tab-page.component.css']
})
export class TabPageComponent implements OnInit {

  constructor(private api: ApiService) { }

  ngOnInit() {

  }

}
