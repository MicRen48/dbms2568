-- 1. doctor
CREATE TABLE doctor (
    doctor_id INT PRIMARY KEY,
    ssn VARCHAR (13),
    name VARCHAR (50),
    specialty VARCHAR (100),
    experience_year INT
);

-- 2. patient (อ้างอิง doctor_id)
CREATE TABLE patient (
    patient_id INT PRIMARY KEY,
    ssn VARCHAR (13),
    name VARCHAR (50),
    address VARCHAR (100),
    age INT,
    doctor_id INT,
    FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id)
);

-- 3. drug
CREATE TABLE drug (
    drug_id INT PRIMARY KEY,
    trade_name VARCHAR (100),
    formula VARCHAR (100)
);

-- 4. pharmacy
CREATE TABLE pharmacy (
    pharmacy_id INT PRIMARY KEY,
    name VARCHAR (100),
    address VARCHAR (200),
    phone VARCHAR (10)
);

-- 5. pharm_co
CREATE TABLE pharm_co (
    pharm_co_id INT PRIMARY KEY,
    name VARCHAR (100),
    phone VARCHAR (13)
);

-- 6. prescription (อ้างอิง patient_id, doctor_id, drug_id)
CREATE TABLE prescription (
    prescription_id INT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    drug_id INT,
    prescription_date DATE,
    quantity INT,
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id),
    FOREIGN KEY (drug_id) REFERENCES drug(drug_id)
);

-- 7. sell (ตารางความสัมพันธ์: pharmacy ขาย drug)
CREATE TABLE sell (
    sell_id INT PRIMARY KEY,
    pharmacy_id INT,
    drug_id INT,
    price NUMERIC,
    FOREIGN KEY (pharmacy_id) REFERENCES pharmacy(pharmacy_id),
    FOREIGN KEY (drug_id) REFERENCES drug(drug_id)
);

-- 8. contract (อ้างอิง pharmacy_id, pharm_co_id, drug_id)
CREATE TABLE contract (
    contract_id INT PRIMARY KEY,
    pharmacy_id INT,
    pharm_co_id INT,
    drug_id INT,
    start_date DATE,
    end_date DATE,
    contract_note VARCHAR (200),
    supervisor VARCHAR (100),
    FOREIGN KEY (pharmacy_id) REFERENCES pharmacy(pharmacy_id),
    FOREIGN KEY (pharm_co_id) REFERENCES pharm_co(pharm_co_id),
    FOREIGN KEY (drug_id) REFERENCES drug(drug_id)
);

SELECT pharmacy.name AS pharmacy,
       pharm_co.name AS pharm_co,
       drug.trade_name AS drug,
       contract.start_date,
       contract.end_date
FROM contract
JOIN pharmacy ON contract.pharmacy_id = pharmacy.pharmacy_id
JOIN pharm_co ON contract.pharm_co_id = pharm_co.pharm_co_id
JOIN drug ON contract.drug_id = drug.drug_id;
