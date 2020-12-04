import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LineScatterPlotComponent } from './line-scatter-plot.component';

describe('LineScatterPlotComponent', () => {
  let component: LineScatterPlotComponent;
  let fixture: ComponentFixture<LineScatterPlotComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LineScatterPlotComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LineScatterPlotComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
