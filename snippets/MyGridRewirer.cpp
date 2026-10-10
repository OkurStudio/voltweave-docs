#include "MyGridRewirer.h"

#include "Components/VWVNodeComponent.h"
#include "Components/VWVSourceComponent.h"
#include "VWVBlueprintLibrary.h"
#include "VWVGridSubsystem.h"

void AMyGridRewirer::BeginPlay()
{
	Super::BeginPlay();

	if (!HasAuthority())
	{
		return;
	}
	if (UVWVGridSubsystem* Grid = UVWVGridSubsystem::Get(this))
	{
		Grid->OnNodeRegisteredNative().AddUObject(this, &AMyGridRewirer::HandleNodeRegistered);
	}
}

void AMyGridRewirer::HandleNodeRegistered(UVWVNodeComponent* Node)
{
	if (!IsValid(Node) || Node->GetOwner() != LampActor)
	{
		return;
	}
	if (UVWVNodeComponent* Source = UVWVBlueprintLibrary::FindGridNode(GeneratorActor, UVWVSourceComponent::StaticClass()))
	{
		Source->ConnectTo(Node);
	}
}
