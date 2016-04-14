#!/usr/bin/env bash
#export GOOGLE_APPLICATION_CREDENTIALS=Dataflow\ Demo-a647d429d25d.json

for i in {1..20}
do
    mvn compile exec:java -Dexec.mainClass=com.google.cloud.dataflow.examples.complete.game.injector.Injector -Dexec.args="df-demo injected none" &
done

