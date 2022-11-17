{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7J_Ld7naD4Ov",
        "outputId": "a2f3a902-7ceb-4099-db3e-663262710713"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "updated-Xception-diabetic-retinopathy-final.h5\n"
          ]
        }
      ],
      "source": [
        "!tar -zcvf xception-diabetic-retinopathy-final.tgz updated-Xception-diabetic-retinopathy-final.h5"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3z3nVOOGFgQF",
        "outputId": "05f92ad7-40c7-495c-8ef7-137946c15950"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting ibm_watson_machine_learning\n",
            "  Downloading ibm_watson_machine_learning-1.0.257-py3-none-any.whl (1.8 MB)\n",
            "\u001b[K     |████████████████████████████████| 1.8 MB 7.4 MB/s \n",
            "\u001b[?25hRequirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (from ibm_watson_machine_learning) (2.23.0)\n",
            "Requirement already satisfied: pandas<1.5.0,>=0.24.2 in /usr/local/lib/python3.7/dist-packages (from ibm_watson_machine_learning) (1.3.5)\n",
            "Collecting ibm-cos-sdk==2.7.*\n",
            "  Downloading ibm-cos-sdk-2.7.0.tar.gz (51 kB)\n",
            "\u001b[K     |████████████████████████████████| 51 kB 703 kB/s \n",
            "\u001b[?25hRequirement already satisfied: tabulate in /usr/local/lib/python3.7/dist-packages (from ibm_watson_machine_learning) (0.8.10)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.7/dist-packages (from ibm_watson_machine_learning) (2022.9.24)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.7/dist-packages (from ibm_watson_machine_learning) (21.3)\n",
            "Requirement already satisfied: urllib3 in /usr/local/lib/python3.7/dist-packages (from ibm_watson_machine_learning) (1.24.3)\n",
            "Collecting lomond\n",
            "  Downloading lomond-0.3.3-py2.py3-none-any.whl (35 kB)\n",
            "Requirement already satisfied: importlib-metadata in /usr/local/lib/python3.7/dist-packages (from ibm_watson_machine_learning) (4.13.0)\n",
            "Collecting ibm-cos-sdk-core==2.7.0\n",
            "  Downloading ibm-cos-sdk-core-2.7.0.tar.gz (824 kB)\n",
            "\u001b[K     |████████████████████████████████| 824 kB 55.6 MB/s \n",
            "\u001b[?25hCollecting ibm-cos-sdk-s3transfer==2.7.0\n",
            "  Downloading ibm-cos-sdk-s3transfer-2.7.0.tar.gz (133 kB)\n",
            "\u001b[K     |████████████████████████████████| 133 kB 46.2 MB/s \n",
            "\u001b[?25hCollecting jmespath<1.0.0,>=0.7.1\n",
            "  Downloading jmespath-0.10.0-py2.py3-none-any.whl (24 kB)\n",
            "Collecting docutils<0.16,>=0.10\n",
            "  Downloading docutils-0.15.2-py3-none-any.whl (547 kB)\n",
            "\u001b[K     |████████████████████████████████| 547 kB 46.8 MB/s \n",
            "\u001b[?25hRequirement already satisfied: python-dateutil<3.0.0,>=2.1 in /usr/local/lib/python3.7/dist-packages (from ibm-cos-sdk-core==2.7.0->ibm-cos-sdk==2.7.*->ibm_watson_machine_learning) (2.8.2)\n",
            "Requirement already satisfied: numpy>=1.17.3 in /usr/local/lib/python3.7/dist-packages (from pandas<1.5.0,>=0.24.2->ibm_watson_machine_learning) (1.21.6)\n",
            "Requirement already satisfied: pytz>=2017.3 in /usr/local/lib/python3.7/dist-packages (from pandas<1.5.0,>=0.24.2->ibm_watson_machine_learning) (2022.6)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/dist-packages (from python-dateutil<3.0.0,>=2.1->ibm-cos-sdk-core==2.7.0->ibm-cos-sdk==2.7.*->ibm_watson_machine_learning) (1.15.0)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests->ibm_watson_machine_learning) (3.0.4)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests->ibm_watson_machine_learning) (2.10)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata->ibm_watson_machine_learning) (3.10.0)\n",
            "Requirement already satisfied: typing-extensions>=3.6.4 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata->ibm_watson_machine_learning) (4.1.1)\n",
            "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging->ibm_watson_machine_learning) (3.0.9)\n",
            "Building wheels for collected packages: ibm-cos-sdk, ibm-cos-sdk-core, ibm-cos-sdk-s3transfer\n",
            "  Building wheel for ibm-cos-sdk (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for ibm-cos-sdk: filename=ibm_cos_sdk-2.7.0-py2.py3-none-any.whl size=72563 sha256=0c70e272e3b1afabc356b753e1f9bf4f38512a3448baf596047fffb9089760b7\n",
            "  Stored in directory: /root/.cache/pip/wheels/47/22/bf/e1154ff0f5de93cc477acd0ca69abfbb8b799c5b28a66b44c2\n",
            "  Building wheel for ibm-cos-sdk-core (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for ibm-cos-sdk-core: filename=ibm_cos_sdk_core-2.7.0-py2.py3-none-any.whl size=501013 sha256=65e04647df3ff68559568f92c61c0b3ff08f750d7593f6d8e025e0d755bb8b3a\n",
            "  Stored in directory: /root/.cache/pip/wheels/6c/a2/e4/c16d02f809a3ea998e17cfd02c13369281f3d232aaf5902c19\n",
            "  Building wheel for ibm-cos-sdk-s3transfer (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for ibm-cos-sdk-s3transfer: filename=ibm_cos_sdk_s3transfer-2.7.0-py2.py3-none-any.whl size=88622 sha256=24b5e6a011c2c93f956720d076a3163c38f53f523cef67525d074e328183cb6c\n",
            "  Stored in directory: /root/.cache/pip/wheels/5f/b7/14/fbe02bc1ef1af890650c7e51743d1c83890852e598d164b9da\n",
            "Successfully built ibm-cos-sdk ibm-cos-sdk-core ibm-cos-sdk-s3transfer\n",
            "Installing collected packages: jmespath, docutils, ibm-cos-sdk-core, ibm-cos-sdk-s3transfer, lomond, ibm-cos-sdk, ibm-watson-machine-learning\n",
            "  Attempting uninstall: docutils\n",
            "    Found existing installation: docutils 0.17.1\n",
            "    Uninstalling docutils-0.17.1:\n",
            "      Successfully uninstalled docutils-0.17.1\n",
            "Successfully installed docutils-0.15.2 ibm-cos-sdk-2.7.0 ibm-cos-sdk-core-2.7.0 ibm-cos-sdk-s3transfer-2.7.0 ibm-watson-machine-learning-1.0.257 jmespath-0.10.0 lomond-0.3.3\n"
          ]
        }
      ],
      "source": [
        "!pip install ibm_watson_machine_learning"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8JoCK6dfF_WJ",
        "outputId": "675a28e4-7838-437b-e7ee-4e4dcbef00c2"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Python 3.7 and 3.8 frameworks are deprecated and will be removed in a future release. Use Python 3.9 framework instead.\n"
          ]
        }
      ],
      "source": [
        "from ibm_watson_machine_learning import APIClient\n",
        "\n",
        "wml_credentials = {\n",
        "    'url':'https://us-south.ml.cloud.ibm.com',\n",
        "    'apikey':'Kh4eF5CXk72w0wGCsM_KUiXCVjsCcT4a54UKVXckt1Bv'\n",
        "}\n",
        "\n",
        "client = APIClient(wml_credentials)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cT0cytAdI5ta",
        "outputId": "2951591f-3ca0-4fa8-aaa2-1d483112d892"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "<ibm_watson_machine_learning.client.APIClient at 0x7f4ab66959d0>"
            ]
          },
          "execution_count": 30,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "client"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YIWuKH5qJGGq",
        "outputId": "da5acf1a-f8c4-4f65-9dee-b42388f52929"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "{'resources': [{'entity': {'compute': [{'crn': 'crn:v1:bluemix:public:pm-20:us-south:a/2a86aebdf8c547c0b1fcb47643309408:2758970b-1c34-4f64-b466-83ed89aaf984::',\n",
              "      'guid': '2758970b-1c34-4f64-b466-83ed89aaf984',\n",
              "      'name': 'Watson Machine Learning-wo',\n",
              "      'type': 'machine_learning'}],\n",
              "    'description': '',\n",
              "    'name': 'Diabetic_Retinopathy',\n",
              "    'scope': {'bss_account_id': '2a86aebdf8c547c0b1fcb47643309408'},\n",
              "    'stage': {'production': False},\n",
              "    'status': {'state': 'active'},\n",
              "    'storage': {'properties': {'bucket_name': '23fc0d3c-c59e-4777-923d-7ab75fcf300f',\n",
              "      'bucket_region': 'us-south',\n",
              "      'credentials': {'admin': {'access_key_id': '141b4866bc4244a0b54132e1d9637393',\n",
              "        'api_key': '8NwpRcRd354DGxdTvfeLyg94BbGoYsqzly6-I4Ihz8mE',\n",
              "        'secret_access_key': '89d8dc94b88ea77a8512a4e500a88555cfd84fe5f697afac',\n",
              "        'service_id': 'ServiceId-17d23243-ca8b-4e08-82f5-c0e4095076c5'},\n",
              "       'editor': {'access_key_id': 'b822a6a9d6d84ed798e98cfd5e8f5249',\n",
              "        'api_key': 'OgwD6g31HNEaUNaI3k7VuJv03PVsVFVRd15EfsosHVnl',\n",
              "        'resource_key_crn': 'crn:v1:bluemix:public:cloud-object-storage:global:a/2a86aebdf8c547c0b1fcb47643309408:54c53eab-929e-4d1d-983f-2274cac80845::',\n",
              "        'secret_access_key': 'ac08ce99330affa66919332e9a897fae07d1b5c8d74423d4',\n",
              "        'service_id': 'ServiceId-188f7888-141c-4102-a9c7-419363e5c5a6'},\n",
              "       'viewer': {'access_key_id': 'dd87ca6d9ded449b83be4cbdd0aa797f',\n",
              "        'api_key': 'mbBJdoKsaEND9QKd0FC_mp5G_Fn_0W-BYLZ2zvyNzMTo',\n",
              "        'resource_key_crn': 'crn:v1:bluemix:public:cloud-object-storage:global:a/2a86aebdf8c547c0b1fcb47643309408:54c53eab-929e-4d1d-983f-2274cac80845::',\n",
              "        'secret_access_key': 'ed71264ffa92b2bd54c4a3ff9214f27062e25002887ce5cd',\n",
              "        'service_id': 'ServiceId-f729cd0a-7956-4e3f-a8c2-177a4e928eb4'}},\n",
              "      'endpoint_url': 'https://s3.us-south.cloud-object-storage.appdomain.cloud',\n",
              "      'guid': '54c53eab-929e-4d1d-983f-2274cac80845',\n",
              "      'resource_crn': 'crn:v1:bluemix:public:cloud-object-storage:global:a/2a86aebdf8c547c0b1fcb47643309408:54c53eab-929e-4d1d-983f-2274cac80845::'},\n",
              "     'type': 'bmcos_object_storage'}},\n",
              "   'metadata': {'created_at': '2022-11-13T07:25:46.815Z',\n",
              "    'creator_id': 'IBMid-666002L8CV',\n",
              "    'id': '0635fbc4-6bb7-439d-8cec-4058d2d6a6f9',\n",
              "    'updated_at': '2022-11-13T07:26:04.510Z',\n",
              "    'url': '/v2/spaces/0635fbc4-6bb7-439d-8cec-4058d2d6a6f9'}},\n",
              "  {'entity': {'compute': [{'crn': 'crn:v1:bluemix:public:pm-20:us-south:a/2a86aebdf8c547c0b1fcb47643309408:2758970b-1c34-4f64-b466-83ed89aaf984::',\n",
              "      'guid': '2758970b-1c34-4f64-b466-83ed89aaf984',\n",
              "      'name': 'Watson Machine Learning-wo',\n",
              "      'type': 'machine_learning'}],\n",
              "    'description': '',\n",
              "    'name': 'Diabetic_Retinopathy_Final',\n",
              "    'scope': {'bss_account_id': '2a86aebdf8c547c0b1fcb47643309408'},\n",
              "    'stage': {'production': False},\n",
              "    'status': {'state': 'active'},\n",
              "    'storage': {'properties': {'bucket_name': 'a03023d3-bd13-4056-9a5c-bd42877e3d37',\n",
              "      'bucket_region': 'us-south',\n",
              "      'credentials': {'admin': {'access_key_id': 'b75d15c579ca49d39ce6035769f38085',\n",
              "        'api_key': 'WCgfy_VKIN6ZxrP7RM7aklOx3NiAToICqFvgDQe1Htka',\n",
              "        'secret_access_key': 'c58cff5b94b462cbb562003c731e897eb5870c5ac58fd3f1',\n",
              "        'service_id': 'ServiceId-6cdfe7ea-8289-4d59-af2e-6793ff189770'},\n",
              "       'editor': {'access_key_id': 'cec1ba6cd57741b0886239516ca26e31',\n",
              "        'api_key': 'N0Av9ZzsyzxF68V434G5HK971Txq1IBHjBmIf9I6OGQ6',\n",
              "        'resource_key_crn': 'crn:v1:bluemix:public:cloud-object-storage:global:a/2a86aebdf8c547c0b1fcb47643309408:54c53eab-929e-4d1d-983f-2274cac80845::',\n",
              "        'secret_access_key': '60dcce7cbcb1485d44358ee02076556bd0f73dd523cc4e20',\n",
              "        'service_id': 'ServiceId-e5af9e90-45c9-47c4-b93d-be9c5b4aea56'},\n",
              "       'viewer': {'access_key_id': '1289a05a65674d629ac9398c52a9e731',\n",
              "        'api_key': 'N4lh4A3I6LRGNKbpC7O31Ol_cdk5ZsjR9yc2sx0FQ0ns',\n",
              "        'resource_key_crn': 'crn:v1:bluemix:public:cloud-object-storage:global:a/2a86aebdf8c547c0b1fcb47643309408:54c53eab-929e-4d1d-983f-2274cac80845::',\n",
              "        'secret_access_key': '2c75c7e51f9cf09007b50493613eb96f79efb2226962af2a',\n",
              "        'service_id': 'ServiceId-cabb204e-efd9-4022-b3b9-4f52dd71908e'}},\n",
              "      'endpoint_url': 'https://s3.us-south.cloud-object-storage.appdomain.cloud',\n",
              "      'guid': '54c53eab-929e-4d1d-983f-2274cac80845',\n",
              "      'resource_crn': 'crn:v1:bluemix:public:cloud-object-storage:global:a/2a86aebdf8c547c0b1fcb47643309408:54c53eab-929e-4d1d-983f-2274cac80845::'},\n",
              "     'type': 'bmcos_object_storage'}},\n",
              "   'metadata': {'created_at': '2022-11-13T12:59:23.453Z',\n",
              "    'creator_id': 'IBMid-666002L8CV',\n",
              "    'id': '390d15db-1863-40c5-8be1-f9985867d94a',\n",
              "    'updated_at': '2022-11-13T12:59:40.608Z',\n",
              "    'url': '/v2/spaces/390d15db-1863-40c5-8be1-f9985867d94a'}}]}"
            ]
          },
          "execution_count": 31,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "client.spaces.get_details()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vBia0O2BJMVG",
        "outputId": "3361659c-1c97-4043-84c2-ce20cbd91a12"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Note: 'limit' is not provided. Only first 50 records will be displayed if the number of records exceed 50\n",
            "------------------------------------  --------------------------  ------------------------\n",
            "ID                                    NAME                        CREATED\n",
            "390d15db-1863-40c5-8be1-f9985867d94a  Diabetic_Retinopathy_Final  2022-11-13T12:59:23.453Z\n",
            "0635fbc4-6bb7-439d-8cec-4058d2d6a6f9  Diabetic_Retinopathy        2022-11-13T07:25:46.815Z\n",
            "------------------------------------  --------------------------  ------------------------\n"
          ]
        }
      ],
      "source": [
        "client.spaces.list()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "rbvtBITJoDO_"
      },
      "outputs": [],
      "source": [
        "space_uid = \"390d15db-1863-40c5-8be1-f9985867d94a\""
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "qi4LOvDBoskq",
        "outputId": "3982c02e-6d56-4ea4-fc25-7dec56d0c779"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'SUCCESS'"
            ]
          },
          "execution_count": 34,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "client.set.default_space(space_uid)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MZJdbLt1o_xU",
        "outputId": "c79b45c3-19c8-44e8-d46b-96dd2758db2e"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "-----------------------------  ------------------------------------  ----\n",
            "NAME                           ASSET_ID                              TYPE\n",
            "default_py3.6                  0062b8c9-8b7d-44a0-a9b9-46c416adcbd9  base\n",
            "kernel-spark3.2-scala2.12      020d69ce-7ac1-5e68-ac1a-31189867356a  base\n",
            "pytorch-onnx_1.3-py3.7-edt     069ea134-3346-5748-b513-49120e15d288  base\n",
            "scikit-learn_0.20-py3.6        09c5a1d0-9c1e-4473-a344-eb7b665ff687  base\n",
            "spark-mllib_3.0-scala_2.12     09f4cff0-90a7-5899-b9ed-1ef348aebdee  base\n",
            "pytorch-onnx_rt22.1-py3.9      0b848dd4-e681-5599-be41-b5f6fccc6471  base\n",
            "ai-function_0.1-py3.6          0cdb0f1e-5376-4f4d-92dd-da3b69aa9bda  base\n",
            "shiny-r3.6                     0e6e79df-875e-4f24-8ae9-62dcc2148306  base\n",
            "tensorflow_2.4-py3.7-horovod   1092590a-307d-563d-9b62-4eb7d64b3f22  base\n",
            "pytorch_1.1-py3.6              10ac12d6-6b30-4ccd-8392-3e922c096a92  base\n",
            "tensorflow_1.15-py3.6-ddl      111e41b3-de2d-5422-a4d6-bf776828c4b7  base\n",
            "autoai-kb_rt22.2-py3.10        125b6d9a-5b1f-5e8d-972a-b251688ccf40  base\n",
            "runtime-22.1-py3.9             12b83a17-24d8-5082-900f-0ab31fbfd3cb  base\n",
            "scikit-learn_0.22-py3.6        154010fa-5b3b-4ac1-82af-4d5ee5abbc85  base\n",
            "default_r3.6                   1b70aec3-ab34-4b87-8aa0-a4a3c8296a36  base\n",
            "pytorch-onnx_1.3-py3.6         1bc6029a-cc97-56da-b8e0-39c3880dbbe7  base\n",
            "kernel-spark3.3-r3.6           1c9e5454-f216-59dd-a20e-474a5cdf5988  base\n",
            "pytorch-onnx_rt22.1-py3.9-edt  1d362186-7ad5-5b59-8b6c-9d0880bde37f  base\n",
            "tensorflow_2.1-py3.6           1eb25b84-d6ed-5dde-b6a5-3fbdf1665666  base\n",
            "spark-mllib_3.2                20047f72-0a98-58c7-9ff5-a77b012eb8f5  base\n",
            "tensorflow_2.4-py3.8-horovod   217c16f6-178f-56bf-824a-b19f20564c49  base\n",
            "runtime-22.1-py3.9-cuda        26215f05-08c3-5a41-a1b0-da66306ce658  base\n",
            "do_py3.8                       295addb5-9ef9-547e-9bf4-92ae3563e720  base\n",
            "autoai-ts_3.8-py3.8            2aa0c932-798f-5ae9-abd6-15e0c2402fb5  base\n",
            "tensorflow_1.15-py3.6          2b73a275-7cbf-420b-a912-eae7f436e0bc  base\n",
            "kernel-spark3.3-py3.9          2b7961e2-e3b1-5a8c-a491-482c8368839a  base\n",
            "pytorch_1.2-py3.6              2c8ef57d-2687-4b7d-acce-01f94976dac1  base\n",
            "spark-mllib_2.3                2e51f700-bca0-4b0d-88dc-5c6791338875  base\n",
            "pytorch-onnx_1.1-py3.6-edt     32983cea-3f32-4400-8965-dde874a8d67e  base\n",
            "spark-mllib_3.0-py37           36507ebe-8770-55ba-ab2a-eafe787600e9  base\n",
            "spark-mllib_2.4                390d21f8-e58b-4fac-9c55-d7ceda621326  base\n",
            "autoai-ts_rt22.2-py3.10        396b2e83-0953-5b86-9a55-7ce1628a406f  base\n",
            "xgboost_0.82-py3.6             39e31acd-5f30-41dc-ae44-60233c80306e  base\n",
            "pytorch-onnx_1.2-py3.6-edt     40589d0e-7019-4e28-8daa-fb03b6f4fe12  base\n",
            "pytorch-onnx_rt22.2-py3.10     40e73f55-783a-5535-b3fa-0c8b94291431  base\n",
            "default_r36py38                41c247d3-45f8-5a71-b065-8580229facf0  base\n",
            "autoai-ts_rt22.1-py3.9         4269d26e-07ba-5d40-8f66-2d495b0c71f7  base\n",
            "autoai-obm_3.0                 42b92e18-d9ab-567f-988a-4240ba1ed5f7  base\n",
            "pmml-3.0_4.3                   493bcb95-16f1-5bc5-bee8-81b8af80e9c7  base\n",
            "spark-mllib_2.4-r_3.6          49403dff-92e9-4c87-a3d7-a42d0021c095  base\n",
            "xgboost_0.90-py3.6             4ff8d6c2-1343-4c18-85e1-689c965304d3  base\n",
            "pytorch-onnx_1.1-py3.6         50f95b2a-bc16-43bb-bc94-b0bed208c60b  base\n",
            "autoai-ts_3.9-py3.8            52c57136-80fa-572e-8728-a5e7cbb42cde  base\n",
            "spark-mllib_2.4-scala_2.11     55a70f99-7320-4be5-9fb9-9edb5a443af5  base\n",
            "spark-mllib_3.0                5c1b0ca2-4977-5c2e-9439-ffd44ea8ffe9  base\n",
            "autoai-obm_2.0                 5c2e37fa-80b8-5e77-840f-d912469614ee  base\n",
            "spss-modeler_18.1              5c3cad7e-507f-4b2a-a9a3-ab53a21dee8b  base\n",
            "cuda-py3.8                     5d3232bf-c86b-5df4-a2cd-7bb870a1cd4e  base\n",
            "autoai-kb_3.1-py3.7            632d4b22-10aa-5180-88f0-f52dfb6444d7  base\n",
            "pytorch-onnx_1.7-py3.8         634d3cdc-b562-5bf9-a2d4-ea90a478456b  base\n",
            "-----------------------------  ------------------------------------  ----\n",
            "Note: Only first 50 records were displayed. To display more use 'limit' parameter.\n"
          ]
        }
      ],
      "source": [
        "client.software_specifications.list()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "GtG3rcU-pHSk",
        "outputId": "af465cc5-a2fd-4271-d7cb-d701e497ef30"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'acd9c798-6974-5d2f-a657-ce06e986df4d'"
            ]
          },
          "execution_count": 36,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "software_space_uid = client.software_specifications.get_uid_by_name(\"tensorflow_rt22.1-py3.9\")\n",
        "software_space_uid"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "uNpM7IO2rECd"
      },
      "outputs": [],
      "source": [
        "model_details = client.repository.store_model(model=\"xception-diabetic-retinopathy-final.tgz\", meta_props={\n",
        "    client.repository.ModelMetaNames.NAME:\"Diabetic_Retinopathy_Detection\",\n",
        "    client.repository.ModelMetaNames.TYPE:\"tensorflow_2.7\",\n",
        "    client.repository.ModelMetaNames.SOFTWARE_SPEC_UID:software_space_uid\n",
        "})"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Xf9rujfUuZyg",
        "outputId": "323912a7-bc2c-4106-9622-a1b65421ab6b"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "{'entity': {'hybrid_pipeline_software_specs': [],\n",
              "  'software_spec': {'id': 'acd9c798-6974-5d2f-a657-ce06e986df4d',\n",
              "   'name': 'tensorflow_rt22.1-py3.9'},\n",
              "  'type': 'tensorflow_2.7'},\n",
              " 'metadata': {'created_at': '2022-11-13T13:01:40.273Z',\n",
              "  'id': '8fe14029-daff-4ef7-89f9-d23a07f925c2',\n",
              "  'modified_at': '2022-11-13T13:01:47.621Z',\n",
              "  'name': 'Diabetic_Retinopathy_Detection',\n",
              "  'owner': 'IBMid-666002L8CV',\n",
              "  'resource_key': 'f3e58140-1461-4d0b-a852-2bc6197b3863',\n",
              "  'space_id': '390d15db-1863-40c5-8be1-f9985867d94a'},\n",
              " 'system': {'warnings': []}}"
            ]
          },
          "execution_count": 39,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "model_details"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "29Fp_GmWu7cD",
        "outputId": "6512779a-7e48-438f-e421-faf4fcd6f0c6"
      },
      "outputs": [
        {
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'8fe14029-daff-4ef7-89f9-d23a07f925c2'"
            ]
          },
          "execution_count": 40,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "model_id = client.repository.get_model_id(model_details)\n",
        "model_id"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 53
        },
        "id": "BW7WSoJrvd87",
        "outputId": "39b1f3a0-3aae-4a16-ff8f-629f47959dc3"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Successfully saved model content to file: 'Diabetic_Retinopathy_Detection.tgz'\n"
          ]
        },
        {
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'/content/Diabetic_Retinopathy_Detection.tgz'"
            ]
          },
          "execution_count": 41,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "client.repository.download(model_id, 'Diabetic_Retinopathy_Detection.tgz')"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}