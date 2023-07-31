/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"

CRYP_HandleTypeDef hcryp;


//Assemble AES key from memory
uint32_t pKeyAES[8] = {0x01234567,0x89abcdef,0xfedcba98,0x76543210,0x01234567,0x89abcdef,0xfedcba98,0x76543210};

//Read Unique ID from memory
uint32_t iD_1 = 0x01234567;
uint32_t iD_2 = 0x89abcdef;
uint32_t iD_3 = 0xfedcba89;


const uint32_t data_Date = 0x0134b248;
const uint32_t data_Time = 0x0003704f;
const uint32_t data_Data_1 = 0x01234567;
const uint32_t data_Data_2 = 0x89abcdef;

//Assemble data package for encryption
uint32_t input_data[4]={data_Date, data_Time, data_Data_1, data_Data_2};

//Output encrypted data
uint32_t encrypted_data[4];


void SystemClock_Config(void);
static void MX_MEMORYMAP_Init(void);
static void MX_AES_Init(void);

int main(void)
{

  HAL_Init();


  //Encrypt data package using Cryp library
  HAL_CRYP_Encrypt(&hcryp, input_data, 4, encrypted_data, 1000);

/* DATA ENCRYPTED READY FOR SENDING*/

  while (1)
  {
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}
