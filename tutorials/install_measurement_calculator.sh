#!/bin/bash

echo "Installing Measurement Calculator..."
echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

echo "Installing Python3 if not installed..."
sudo apt install -y python3 python3-pip

echo "Creating a directory for the calculator..."
mkdir -p ~/measurement_calculator
cp measurement_calculator.py ~/measurement_calculator/

echo "Creating a run script..."
echo -e "#!/bin/bash\npython3 ~/measurement_calculator/measurement_calculator.py" > ~/measurement_calculator/run_calculator.sh
chmod +x ~/measurement_calculator/run_calculator.sh

echo "Installation complete!"
echo "To run the calculator, use: ~/measurement_calculator/run_calculator.sh"
