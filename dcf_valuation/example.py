from model import DCFValuation

def run_valuation_example():
    # Initialize model
    dcf = DCFValuation("Sample Company")

    # Set parameters with more realistic values
    dcf.set_initial_parameters(
        revenue=1000000000,      # $1B revenue
        ebit_margin=0.15,        # 15% EBIT margin
        beta=1.2,                # Above market volatility
        terminal_growth=0.02,    # 2% terminal growth
        tax_rate=0.25           # 25% tax rate
    )

    # Calculate valuation
    dcf.calculate_wacc()
    dcf.project_free_cash_flows()
    enterprise_value = dcf.calculate_enterprise_value()
    equity_value = dcf.get_equity_value(net_debt=200000000)

    # Print detailed results for debugging
    print("\nDetailed Valuation Results:")
    print(f"WACC: {dcf.wacc:.2%}")
    print("\nProjected Revenues:")
    for i, rev in enumerate(dcf.revenues):
        print(f"Year {i+1}: ${rev:,.2f}")
    
    print("\nProjected Free Cash Flows:")
    for i, fcf in enumerate(dcf.fcf):
        print(f"Year {i+1}: ${fcf:,.2f}")
    
    print(f"\nPresent Value of FCFs: ${dcf.present_value_fcf:,.2f}")
    print(f"Terminal Value: ${dcf.terminal_value:,.2f}")
    print(f"PV of Terminal Value: ${dcf.present_value_terminal:,.2f}")
    print(f"\nEnterprise Value: ${enterprise_value:,.2f}")
    print(f"Equity Value: ${equity_value:,.2f}")

if __name__ == "__main__":
    run_valuation_example()