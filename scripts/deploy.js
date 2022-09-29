const { ethers } = require("hardhat");

async function main() {
    
    // defining a delay function so we don't get rate limited by alchemy
    const delay = ms => new Promise(res => setTimeout(res, ms));

    // Start deployment, returning a promise that resolves to a contract object
    const EVToken = await ethers.getContractFactory("EVToken");
    total_supply = 30
    expiration_time = 5
    const evtoken = await EVToken.deploy(total_supply, expiration_time);
    console.log("EVToken contract deployed to address:", evtoken.address);

    await delay(5000);

    const SubjectAttribute = await ethers.getContractFactory("SubjectAttribute");
    const subjectattribute = await SubjectAttribute.deploy();
    console.log("SubjectAttribute contract deployed to address:", subjectattribute.address);

    await delay(5000);

    const PolicyManagement = await ethers.getContractFactory("PolicyManagement");
    const policymanagement = await PolicyManagement.deploy();
    console.log("PolicyManagement contract deployed to address:", policymanagement.address);

    await delay(5000);

    const ObjectAttribute = await ethers.getContractFactory("ObjectAttribute");
    const objectattribute = await ObjectAttribute.deploy();
    console.log("ObjectAttribute contract deployed to address:", objectattribute.address);

    await delay(5000);

    // addresses for goerli
    // subjectattribute_address = "0x40Bc758DFb8bb04A955616d2Cef31A6C687F03Cc"
    // objectattribute_address = "0x1665E701888F30cecDeaBde94a4D2598dbC68aeA"
    // policymanagement_address = "0x72Ce4D901f36feEF6924d9757D086f61D44b6139"
    // evtoken_address = "0xd3F05FcB61334E4B0F1486051e4E2d6fFA9e03A3"
    // accesscontrol_address = "0xf6B521CD69ae38c2e3231e2d2A74c8E7ECB5a408"

    // addresses for Polygon Mumbai
    // subjectattribute_address = "0x0a016F48c77b4b10C3964B1efDD81d1f51ca4F80"
    // objectattribute_address = "0xFF032FC8DdDFEc8A85df2C1e467dDC3E64B52266"
    // policymanagement_address = "0xFf5505dfA781D42dc55f665190D684c3cA0D6929"
    // evtoken_address = "0xF29a4d0b3B14fC5821AFa4F11506423a68a0D0b4"
    // accesscontrol_address = "0xd94D00Bc72dc7bDeF966360F5ECDC833f2d9eDF7"

    subjectattribute_address = subjectattribute.address
    objectattribute_address = objectattribute.address
    policymanagement_address = policymanagement.address
    evtoken_address = evtoken.address

    const AccessControl = await ethers.getContractFactory("AccessControl");
    const accesscontrol = await AccessControl.deploy(
        subjectattribute_address,
        objectattribute_address,
        policymanagement_address,
        evtoken_address
    );
    console.log("AccessControl contract deployed to address:", accesscontrol.address);  
}

main()
    .then(() => process.exit(0))
    .catch(error => {
        console.error(error);
        process.exit(1);
});