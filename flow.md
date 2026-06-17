START
  ↓
Welcome
  ↓
SelectInsuranceType
  ↓
EnterLicensePlate
  ↓
ValidateLicensePlate
  ├── Invalid → EnterLicensePlate
  ↓
FetchVehicleInfo
  ↓
HandleVehicleResult
  ├── Not Found → EnterLicensePlate
  ├── API Error → RetryOrManualFallback
  │                 ├── Retry → FetchVehicleInfo
  │                 └── Manual / Exit
  ↓
ConfirmVehicle
  ├── No → EnterLicensePlate
  ↓
CollectCustomerDetails
  ↓
ValidateCustomerDetails
  ├── Invalid → CollectCustomerDetails
  ↓
RouteByInsuranceType
  ├── Mandatory → Summary
  └── Comprehensive → AdditionalCoverages
                         ↓
                       Summary
  ↓
EditOrApprove
  ├── Edit Insurance Type → SelectInsuranceType
  │                           ↓
  │                    RouteAfterInsuranceChange
  │                           ├── Mandatory → Summary
  │                           └── Comprehensive → AdditionalCoverages → Summary
  │
  ├── Edit Vehicle → EnterLicensePlate
  │                    ↓
  │              FetchVehicleInfo → ConfirmVehicle → Summary
  │
  ├── Edit Customer Details → CollectCustomerDetails
  │                              ↓
  │                       ValidateCustomerDetails → Summary
  │
  ├── Edit Coverages → AdditionalCoverages → Summary
  │
  └── Approve → FinalConfirmation