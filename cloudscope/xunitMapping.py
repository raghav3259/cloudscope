
xunitMapping = {"mappings": {
                    "testjob": {
                        "properties": {
                            "duration": {
                                "type": "long"
                            },
                            "id": {
                                "type": "long"
                            },
                            "estimatedDuration": {
                                "type": "long"
                            },
                            "name": {
                                "type": "string"
                            },
                            "result": {
                                "type": "string"
                            },
                            "time": {
                                "type": "date"
                            },
                            "changeSet": {
                                "items": {
                                    "author": {
                                        "fullName": {
                                            "type": "string"
                                        }
                                    }
                                }
                            },
                            "culprits": {
                                "fullName": {
                                    "type": "string"
                                }
                            }
                        }
                    },
                    "testsuite": {
                        "_parent": {
                            "type": "testjob"
                        }
                    },
                    "testcase": {
                        "_parent": {
                            "type": "testsuite"
                        }
                    }
}
}
