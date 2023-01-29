from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str
    test_file_path:str


@dataclass
class DataValidationArtifact:
    report_file_path:str


@dataclass
class DataTransformationArtifact:
    transform_train_path:str
    transform_test_path:str
    JetAirways_train_path:str
    JetAirways_test_path:str
    Indigo_train_path:str
    Indigo_test_path:str
    AirIndia_train_path:str
    AirIndia_test_path:str
    MultipleCarriers_train_path:str
    MultipleCarriers_test_path:str
    SpiceJet_train_path:str
    SpiceJet_test_path:str
    Vistara_train_path:str
    Vistara_test_path:str
    AirAsia_train_path:str
    AirAsia_test_path:str
    GoAir_train_path:str
    GoAir_test_path:str

class ModelTrainingArtifact:...
class ModelEvaluationArtifact:...
class ModelPusherArtifact:...