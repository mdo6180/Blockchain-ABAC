from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
from dotenv import load_dotenv
import os


class EVTokenContract:

    def __init__(self, WALLET_ADDRESS: str, EVTOKEN_CONTRACT_ADDRESS: str, API_URL: str) -> None:
        self.WALLET_ADDRESS = WALLET_ADDRESS
        self.EVTOKEN_CONTRACT_ADDRESS = EVTOKEN_CONTRACT_ADDRESS
        
        self.w3 = Web3(Web3.HTTPProvider(API_URL))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    def get_total_supply(self):
        with open("../artifacts/contracts/EVToken.sol/EVToken.json") as evtokenfile:
            artifact = json.load(evtokenfile)
            contract_abi = artifact["abi"]

            evtoken_contract = self.w3.eth.contract(
                address=self.EVTOKEN_CONTRACT_ADDRESS,
                abi=contract_abi
            )

            return evtoken_contract.functions.get_total_supply().call()

    def get_balance(self):
        with open("../artifacts/contracts/EVToken.sol/EVToken.json") as evtokenfile:
            artifact = json.load(evtokenfile)
            contract_abi = artifact["abi"]
            
            evtoken_contract = self.w3.eth.contract(
                address=self.EVTOKEN_CONTRACT_ADDRESS,
                abi=contract_abi
            )

            return evtoken_contract.functions.get_balance(self.WALLET_ADDRESS).call()

    def transfer(self, receiver_address: str, num_tokens: int):
        """
        Transfers tokens from your account to the receiver

        Args:
            receiver_address: 
                The receiver's wallet address in hex form represented as a string
            num_tokens: 
                The number of tokens to send to the receiver (int)
        """

        with open("../artifacts/contracts/EVToken.sol/EVToken.json") as evtokenfile:
            artifact = json.load(evtokenfile)
            contract_abi = artifact["abi"]
            
            evtoken_contract = self.w3.eth.contract(
                address=self.EVTOKEN_CONTRACT_ADDRESS,
                abi=contract_abi
            )

            tx_hash = evtoken_contract.functions.transfer(receiver_address, num_tokens).transact({"from": self.WALLET_ADDRESS})
            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)

            #return tx_hash, tx_receipt
    
    def approve_transaction(self, delegate_address: str, num_tokens: int):
        with open("../artifacts/contracts/EVToken.sol/EVToken.json") as evtokenfile:
            artifact = json.load(evtokenfile)
            contract_abi = artifact["abi"]
            
            evtoken_contract = self.w3.eth.contract(
                address=self.EVTOKEN_CONTRACT_ADDRESS,
                abi=contract_abi
            )

            tx_hash = evtoken_contract.functions.approve(delegate_address, num_tokens).transact({"from": self.WALLET_ADDRESS})

            return tx_hash


if __name__ == "__main__":

    load_dotenv("../.env")
    WALLET_ADDRESS_1 = os.getenv("WALLET_ADDRESS_1")
    WALLET_ADDRESS_2 = os.getenv("WALLET_ADDRESS_2")
    EVTOKEN_CONTRACT_ADDRESS = os.getenv("EVTOKEN_CONTRACT_ADDRESS")
    MUMBAI_API_URL = os.getenv("MUMBAI_API_URL")

    evtokencontract_1 = EVTokenContract(
        WALLET_ADDRESS=WALLET_ADDRESS_1,
        EVTOKEN_CONTRACT_ADDRESS=EVTOKEN_CONTRACT_ADDRESS,
        API_URL=MUMBAI_API_URL
    )

    evtokencontract_2 = EVTokenContract(
        WALLET_ADDRESS=WALLET_ADDRESS_2,
        EVTOKEN_CONTRACT_ADDRESS=EVTOKEN_CONTRACT_ADDRESS,
        API_URL=MUMBAI_API_URL
    )
    
    print(evtokencontract_1.get_total_supply())
    print(evtokencontract_1.get_balance())

    """
    tx_hash= evtokencontract_1.transfer(
        receiver_address=WALLET_ADDRESS_2, 
        num_tokens=1
    )
    """
    
    """
    tx_hash= evtokencontract_1.approve_transaction(
        delegate_address=WALLET_ADDRESS_2, 
        num_tokens=1
    )
    """
    #print(evtokencontract_1.get_total_supply())
    print(evtokencontract_1.get_balance())
    print(evtokencontract_2.get_balance())