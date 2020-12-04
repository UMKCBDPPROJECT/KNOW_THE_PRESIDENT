import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BarGraphNNPComponent } from './bar-graph-nnp.component';

describe('BarGraphNNPComponent', () => {
  let component: BarGraphNNPComponent;
  let fixture: ComponentFixture<BarGraphNNPComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BarGraphNNPComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BarGraphNNPComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
