#!/usr/bin/env bash
mvn compile exec:java -Dexec.mainClass=com.google.cloud.dataflow.examples.complete.game.LeaderBoard -Dexec.args="--project=df-demo --stagingLocation=gs://df-demo-staging --runner=BlockingDataflowPipelineRunner --dataset=df_demo --topic=projects/df-demo/topics/injected"
