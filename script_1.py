
import csv

# Create a comparison table of development frameworks
frameworks_comparison = [
    ['Feature', 'Hardhat', 'Truffle Suite', 'Foundry'],
    ['Release Year', '2019', '2015', '2021'],
    ['Language', 'JavaScript/TypeScript', 'JavaScript', 'Solidity'],
    ['Testing Speed', 'Fast', 'Moderate', 'Very Fast'],
    ['Console.log Support', 'Native (console.log)', 'Via Ganache plugin', 'Native (console.log)'],
    ['Error Messages', 'Detailed Solidity stack traces', 'Basic error messages', 'Detailed stack traces'],
    ['Local Blockchain', 'Hardhat Network (built-in)', 'Ganache (separate)', 'Anvil (built-in)'],
    ['Plugin Ecosystem', 'Extensive', 'Moderate', 'Growing'],
    ['Learning Curve', 'Moderate', 'Easy', 'Steep'],
    ['Documentation', 'Excellent', 'Good', 'Good'],
    ['Mainnet Forking', 'Yes', 'Yes (via Ganache)', 'Yes'],
    ['TypeScript Support', 'Native', 'Requires setup', 'Limited'],
    ['Community Size', 'Large and growing', 'Large (established)', 'Growing rapidly'],
    ['Best For', 'Modern dApp development', 'Beginners, traditional workflow', 'Performance-critical testing'],
    ['Gas Reporting', 'Via plugin', 'Via plugin', 'Built-in'],
    ['Deployment Scripts', 'Ignition modules', 'Migration scripts', 'Solidity scripts'],
    ['Debugging Tools', 'Hardhat Console', 'Truffle Debugger', 'Forge debugger'],
    ['Network Configuration', 'hardhat.config.js', 'truffle-config.js', 'foundry.toml']
]

# Save to CSV
with open('framework_comparison.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(frameworks_comparison)

print("Development Framework Comparison Table Created")
print("=" * 100)
for row in frameworks_comparison:
    print(f"{row[0]:<25} | {row[1]:<30} | {row[2]:<30} | {row[3]:<30}")

# Create security vulnerabilities reference table
print("\n\n")
security_vulnerabilities = [
    ['Vulnerability', 'Description', 'Attack Example', 'Prevention Method', 'Severity'],
    ['Reentrancy Attack', 'External call allows re-entering function before state update', 'DAO Hack (2016) - $60M stolen', 'ReentrancyGuard, Checks-Effects-Interactions pattern', 'Critical'],
    ['Integer Overflow/Underflow', 'Arithmetic operations exceed data type limits', 'BatchOverflow Bug (2018)', 'Use Solidity ^0.8.0 or SafeMath library', 'High'],
    ['Access Control Issues', 'Unauthorized users can call privileged functions', 'Parity Wallet Hack (2017)', 'Implement Ownable, RBAC modifiers', 'Critical'],
    ['Timestamp Dependence', 'Miners can manipulate block.timestamp', 'Lottery contract manipulation', 'Avoid block.timestamp for critical logic', 'Medium'],
    ['Front-running Attack', 'Attacker sees pending transaction and submits higher gas', 'DEX front-running', 'Commit-reveal schemes, batch transactions', 'High'],
    ['Denial of Service (DoS)', 'Contract becomes unusable due to resource exhaustion', 'Gas limit attacks on loops', 'Limit loop iterations, use pull over push', 'Medium'],
    ['Logic Errors', 'Flawed business logic in contract', 'Incorrect calculation formulas', 'Thorough testing, formal verification', 'Variable'],
    ['Insecure Randomness', 'Predictable random number generation', 'Gambling contract exploits', 'Use Chainlink VRF or commit-reveal', 'High'],
    ['Unchecked External Calls', 'Failed external calls not properly handled', 'Funds stuck in contracts', 'Check return values, use require()', 'Medium'],
    ['Sybil Attack', 'Multiple fake identities created', 'Vote manipulation', 'KYC verification, identity proofs', 'Critical']
]

with open('security_vulnerabilities.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(security_vulnerabilities)

print("Security Vulnerabilities Reference Table Created")
print("=" * 150)
for i, row in enumerate(security_vulnerabilities):
    if i == 0:
        print(f"{row[0]:<25} | {row[1]:<45} | {row[2]:<35} | {row[3]:<40} | {row[4]:<10}")
        print("-" * 150)
    else:
        print(f"{row[0]:<25} | {row[1]:<45} | {row[2]:<35} | {row[3]:<40} | {row[4]:<10}")

print("\n\nCSV files created successfully:")
print("1. framework_comparison.csv")
print("2. security_vulnerabilities.csv")
