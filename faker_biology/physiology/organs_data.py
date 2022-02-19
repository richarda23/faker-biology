#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 10:20:19 2022

@author: richard
"""


organ_data = {
    "Musculoskeletal system": {
        "Human skeleton": {},
        "Joints": {},
        "Ligaments": {},
        "Muscular system": {},
        "Tendons": {},
    },
    "Digestive system": {
        "Mouth": {"Teeth": {}, "Tongue": {}},
        "Salivary glands": {
            "Parotid glands": {},
            "Submandibular glands": {},
            "Sublingual glands": {},
        },
        "Pharynx": {},
        "Esophagus": {},
        "Stomach": {},
        "Small intestine": {"Duodenum": {}, "Jejunum": {}, "Ileum": {}},
        "Large intestine": {
            "Cecum": {},
            "Ascending colon": {},
            "Transverse colon": {},
            "Descending colon": {},
            "Sigmoid colon": {},
        },
        "Rectum": {},
        "Liver": {},
        "Gallbladder": {},
        "Mesentery": {},
        "Pancreas": {},
        "Anal canal": {},
    },
    "Respiratory system": {
        "Nasal cavity": {},
        "Pharynx": {},
        "Larynx": {},
        "Trachea": {},
        "Bronchi": {},
        "Bronchioles": {},
        "Lungs": {},
        "Muscles of breathing": {},
    },
    "Urinary system": {"Kidneys": {}, "Ureter": {}, "Bladder": {}, "Urethra": {}},
    "Female reproductive system": {
        "Internal reproductive organs": {
            "Ovaries": {},
            "Fallopian tubes": {},
            "Uterus": {},
            "Cervix": {},
            "Vagina": {},
        },
        "External reproductive organs": {"Vulva": {}, "Clitoris": {}},
        "Placenta": {},
    },
    "Male reproductive system": {
        "Internal reproductive organs": {
            "Testes": {},
            "Epididymis": {},
            "Vas deferens": {},
            "Seminal vesicles": {},
            "Prostate": {},
            "Bulbourethral glands": {},
        },
        "External reproductive organs": {"Penis": {}, "Scrotum": {}},
    },
    "Endocrine system": {
        "Pituitary gland": {},
        "Pineal gland": {},
        "Thyroid gland": {},
        "Parathyroid glands": {},
        "Adrenal glands": {},
        "Pancreas": {},
    },
    "Circulatory system": {"Heart": {}, "Arteries": {}, "Veins": {}, "Capillaries": {}},
    "Lymphatic system": {
        "Lymphatic vessel": {},
        "Lymph node": {},
        "Bone marrow": {},
        "Thymus": {},
        "Spleen": {},
        "Gut-associated lymphoid tissue": {"Tonsils": {}},
        "Interstitium": {},
    },
    "Nervous system": {
        "Brain": {"Cerebrum": {"Cerebral hemispheres": {}}, "Diencephalon": {}},
        "brainstem": {"Midbrain": {}, "Pons": {}, "Medulla oblongata": {}},
        "Cerebellum": {},
        "spinal cord": {},
        "ventricular system": {"Choroid plexus": {}},
    },
    "Peripheral nervous system": {
        "Nerves": {
            "Cranial nerves": {},
            "Spinal nerves": {},
            "Ganglia": {},
            "Enteric nervous system": {},
        }
    },
    "Sensory organs": {
        "Eye": {"Cornea": {}, "Iris": {}, "Ciliary body": {}, "Lens": {}, "Retina": {}},
        "Ear": {
            "Outer ear": {"Earlobe": {}},
            "Eardrum": {},
            "Middle ear": {"Ossicles": {}},
            "Inner ear": {
                "Cochlea": {},
                "Vestibule of the ear": {},
                "Semicircular canals": {},
            },
        },
        "Olfactory epithelium": {},
        "Tongue": {"Taste buds": {}},
    },
    "Integumentary system": {
        "Mammary glands": {},
        "Skin": {},
        "Subcutaneous tissue": {},
    },
}
