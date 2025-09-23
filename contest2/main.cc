class Employee {

public:
    virtual ~Employee() = default;
    virtual double calculatePay() const = 0;  
};

class HourlyEmployee : public Employee {

private:
    double hoursWorked;
    double hourlyRate;

public:
    HourlyEmployee(double hours, double rate)  : hoursWorked(hours), hourlyRate(rate) {}

    double calculatePay() const {
        return hoursWorked * hourlyRate;
    }
};

class SalariedEmployee : public Employee {

private:
    double monthlySalary;

public:
    SalariedEmployee(double salary) : monthlySalary(salary) {}

    double calculatePay() const {
        return monthlySalary;
    }
};

class CommissionEmployee : public Employee {

private:
    double baseSalary;
    double commissionRate;
    double salesAmount;

public:
    CommissionEmployee(double base, double rate, double sales) : baseSalary(base), commissionRate(rate), salesAmount(sales) {}

    double calculatePay() const {
        return baseSalary + commissionRate * salesAmount;
    }
};


