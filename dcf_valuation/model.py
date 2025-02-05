import numpy as np
import pandas as pd
from datetime import datetime

class DCFValuation:
    def __init__(self, company_name):
        self.company_name = company_name
        self.risk_free_rate = 0.035
        self.market_risk_premium = 0.065
        
    def set_initial_parameters(self, 
                             revenue=0,
                             ebit_margin=0,
                             tax_rate=0.25,
                             beta=1.0,
                             terminal_growth=0.02):
        self.revenue = revenue
        self.ebit_margin = ebit_margin
        self.tax_rate = tax_rate
        self.beta = beta
        self.terminal_growth = terminal_growth

    def project_free_cash_flows(self, years=5):
        self.projection_years = years
        self.revenues = []
        self.fcf = []
        previous_revenue = self.revenue
        
        for year in range(years):
            growth_rate = 0.15 - (year * 0.02)
            current_revenue = previous_revenue * (1 + growth_rate)
            self.revenues.append(current_revenue)
            
            ebit = current_revenue * self.ebit_margin
            tax_payment = ebit * self.tax_rate
            nopat = ebit - tax_payment
            
            # Calculate change in working capital instead of absolute value
            working_capital_change = (current_revenue - previous_revenue) * 0.15
            capex = current_revenue * 0.08
            depreciation = capex * 0.7
            
            fcf = nopat + depreciation - capex - working_capital_change
            self.fcf.append(fcf)
            
            previous_revenue = current_revenue

    def calculate_wacc(self, debt_ratio=0.3):
        self.cost_of_equity = self.risk_free_rate + (self.beta * self.market_risk_premium)
        self.cost_of_debt = self.risk_free_rate + 0.02
        self.after_tax_cost_of_debt = self.cost_of_debt * (1 - self.tax_rate)
        self.wacc = (debt_ratio * self.after_tax_cost_of_debt + 
                     (1 - debt_ratio) * self.cost_of_equity)

    def calculate_enterprise_value(self):
        self.present_value_fcf = 0
        for i, fcf in enumerate(self.fcf):
            self.present_value_fcf += fcf / ((1 + self.wacc) ** (i + 1))
        
        terminal_fcf = self.fcf[-1] * (1 + self.terminal_growth)
        self.terminal_value = terminal_fcf / (self.wacc - self.terminal_growth)
        self.present_value_terminal = self.terminal_value / ((1 + self.wacc) ** self.projection_years)
        self.enterprise_value = self.present_value_fcf + self.present_value_terminal
        return self.enterprise_value

    def get_equity_value(self, net_debt):
        return self.enterprise_value - net_debt