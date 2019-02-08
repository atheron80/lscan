# Copyright (C) 2018 - This notice is to be included in all relevant source files.
# "Brandon Goldbeck" <bpg@pdx.edu>
# “Anthony Namba” <anamba@pdx.edu>
# “Brandon Le” <lebran@pdx.edu>
# “Ann Peake” <peakean@pdx.edu>
# “Sohan Tamang” <sohan@pdx.edu>
# “An Huynh” <an35@pdx.edu>
# “Theron Anderson” <atheron@pdx.edu>
# This software is licensed under the MIT License. See LICENSE file for the full text.
import unittest
from src.log_messages.input_model_message import InputModelMessage
from src.log_messages.log_type import LogType
from src.model_conversion.ldraw_model import LDrawModel
from src.model_conversion.model_shipper import ModelShipper
from util import Util


class TestInputModelMessage(unittest.TestCase):
    """Testing the InputModelMessage class.
    """

    def test_(self):

        # Load the model from the assets folder.
        input_model = ModelShipper.load_stl_model(Util.path_conversion("/assets/models/plane.stl"))
        output_model = LDrawModel(
            "plane",  # Model name
            "Rando",  # Author
            "!LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt",  # License info
            input_model  # Mesh
        )

        test_message = "test output model message"
        log_type = LogType.ERROR
        model_message = InputModelMessage(log_type, test_message, output_model)

        self.assertEqual(model_message.get_message(), test_message)
        self.assertEqual(model_message.get_message_type(), log_type)
        self.assertIsNotNone(model_message.get_timestamp())
        self.assertEqual(model_message.get_model(), output_model)