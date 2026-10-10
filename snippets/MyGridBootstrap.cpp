#include "MyGridBootstrap.h"

#include "Components/VWVConsumerComponent.h"
#include "Components/VWVSourceComponent.h"
#include "VWVBlueprintLibrary.h"

void AMyGridBootstrap::BeginPlay()
{
	Super::BeginPlay();

	// Changing the grid is a server job.
	if (!HasAuthority() || !GeneratorActor || !LampActor)
	{
		return;
	}

	UVWVSourceComponent* Source = Cast<UVWVSourceComponent>(
		UVWVBlueprintLibrary::AddGridNodeToActor(GeneratorActor, UVWVSourceComponent::StaticClass(), TEXT("Power")));
	UVWVConsumerComponent* Lamp = Cast<UVWVConsumerComponent>(
		UVWVBlueprintLibrary::AddGridNodeToActor(LampActor, UVWVConsumerComponent::StaticClass(), TEXT("Power")));
	if (!Source || !Lamp)
	{
		return;
	}

	Source->SetMaxOutputWatts(2000.f);
	Lamp->SetRequestedWatts(100.f);
	Source->ConnectTo(Lamp);
}
