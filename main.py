from Chicken_Disease_Classification import logger
from Chicken_Disease_Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Chicken_Disease_Classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Chicken_Disease_Classification.pipeline.stage_03_training import ModelTrainingPipeline
from Chicken_Disease_Classification.pipeline.stage_04_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f" >>>> Running stage: {STAGE_NAME} started ...")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> Stage Name: {STAGE_NAME} >>>> completed!\n\nx ========= x")
except Exception as e:
    logger.exception(e)
    raise e

print("\n \n")
STAGE_NAME = "Prepare base model"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e 

print("\n \n")
STAGE_NAME = "Training"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

print("\n \n")

STAGE_NAME = "Evaluation stage"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


