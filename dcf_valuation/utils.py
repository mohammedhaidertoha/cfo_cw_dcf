import numpy as np

def calculate_historical_growth(revenues):
    """Calculate historical growth rates from revenue data"""
    growth_rates = []
    for i in range(1, len(revenues)):
        growth_rate = (revenues[i] - revenues[i-1]) / revenues[i-1]
        growth_rates.append(growth_rate)
    return np.mean(growth_rates)

def validate_inputs(parameters):
    """Validate input parameters"""
    required_params = ['revenue', 'ebit_margin', 'beta']
    for param in required_params:
        if param not in parameters:
            raise ValueError(f"Missing required parameter: {param}")