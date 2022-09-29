from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
from dotenv import load_dotenv
import os


class SubjectAttribute:

    def __init__(self, WALLET_ADDRESS: str, SUBJECT_ATTRIBUTE_CONTRACT_ADDRESS: str, API_URL: str) -> None:
        self.WALLET_ADDRESS = WALLET_ADDRESS
        self.SUBJECT_ATTRIBUTE_CONTRACT_ADDRESS = SUBJECT_ATTRIBUTE_CONTRACT_ADDRESS
        
        self.w3 = Web3(Web3.HTTPProvider(API_URL))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    def subject_add(
        self, 
        manufacturer, current_location, vehicle_type, charging_efficiency, 
        discharging_efficiency, energy_capacity, ToMFR
    ):
        with open("../artifacts/contracts/SubjectAttribute.sol/SubjectAttribute.json") as subjectfile:
            artifact = json.load(subjectfile)
            contract_abi = artifact["abi"]
            
            subject_contract = self.w3.eth.contract(
                address=self.SUBJECT_ATTRIBUTE_CONTRACT_ADDRESS,
                abi=contract_abi
            )